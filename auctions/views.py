from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Product,general_categories


def index(request):
    return render(request, "auctions/index.html", {
        "products": Product.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

category_names = [category[1] for category in general_categories]

def categories(request):
    if request.method == "POST":
        category = request.POST["category"]
        print(category)
        return render(request, "auctions/index.html", {
            "products": Product.objects.filter(categories=category),
        })
    return render(request, "auctions/categories.html", {
        "category_names" : category_names,
    })

category_ids = {value:count for count, value in enumerate(category_names, start=1)}

@login_required
def new_listing(request):
    if request.method == "POST" and request.user.is_authenticated:
        new_product = Product(
            title = request.POST["title"],
            description = request.POST["description"],
            bid_value = request.POST["bid_value"],
            categories = category_ids[request.POST["categories"]],
            image_url = request.POST["image_url"],
            seller = request.user,
        )
        new_product.save()
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, "auctions/new_listing.html", {
        "category_names":["-----"]+category_names,
    })
           

def product_listing(request, product_id):
    product = Product.objects.get(pk=product_id)
    isListingInWatchList = request.user in product.watchlist.all()
    return render(request, "auctions/product_listing.html",{
        "product": Product.objects.get(pk=product_id),
        "isListingInWatchList" : isListingInWatchList,
    })

@login_required
def watchlist(request):
    user = request.user
    watchlists = user.ListingWatchList.all()
    return render(request, "auctions/watchlist.html", {
        "products": watchlists,
    })

def addWatchlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    currentuser = request.user
    product.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse('product_listing', args=(product_id, )))

def removeWatchlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    currentuser = request.user
    product.watchlist.remove(currentuser)
    return HttpResponseRedirect(reverse('product_listing', args=(product_id, )))