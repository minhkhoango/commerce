from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass

general_categories = [
    ("1", "Art"),
    ("2", "Electronics"),
    ("3", "Fashion"),
    ("4", "Household item"),
    ("5", "Jewelries"),
    ("6", "Treats"),
]

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    bid_value = models.IntegerField(validators=[MaxValueValidator(1000000), MinValueValidator(1)])
    current_bidder = models.CharField(max_length=150)
    categories = models.CharField(max_length=20, choices=general_categories)
    image_url = models.URLField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="info")
    post_date = models.DateTimeField(auto_now_add=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="ListingWatchList")

    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="BidUser")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="BidProduct")
    offer_bid_value = models.IntegerField()

    def clean(self):
        if self.offer_bid_value < self.product.bid_value:
            raise ValidationError("Offer bid value is cannot be less than the current bid value")

    def __str__(self):
        return f"Bid {self.product.title} at {self.offer_bid_value}"
