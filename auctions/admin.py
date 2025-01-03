from django.contrib import admin

# Register your models here.
from .models import Product, User, Bid, Comment

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment)