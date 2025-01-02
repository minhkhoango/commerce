from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("product_listing/<int:product_id>", views.product_listing, name="product_listing"),
    path("categories", views.categories, name="categories"),
    path("addWatchlist/<int:product_id>", views.addWatchlist, name="addWatchlist"),
    path("removeWatchlist<int:product_id>", views.removeWatchlist, name="removeWatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
]
