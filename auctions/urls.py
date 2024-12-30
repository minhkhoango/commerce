from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:product_id>/product_listing", views.product_listing, name = "product_listing"),
    path("categories", views.categories, name = "categories")
]
