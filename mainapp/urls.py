from django.urls import path

from .views import *



urlpatterns = [
    path("", main, name="home"),
    path("products/", products, name="products"),
    path("products/all", products, name="products_all"),
    path("products/home", products, name="products_home"),
    path("products/office", products, name="products_office"),
    path("products/modern", products, name="products_modern"),
    path("products/classic", products, name="products_classic"),
    path("contact/", contact, name="contact"),
]