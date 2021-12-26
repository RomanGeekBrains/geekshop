from django.urls import path

from .views import *


urlpatterns = [
    path("", main, name='home'),
    path("products/", products, name='products'),
    path("contact/", contact, name='contact'),
]
