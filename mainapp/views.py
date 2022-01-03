import json

from django.conf import settings
from django.shortcuts import render

from .models import Product, ProductCategory


def main(request):
    title = "домашняя"

    products = Product.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"

    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"

    with open("mainapp/data_json/contact_info.json", "r") as file_with_contact_info:
        locations = json.loads(file_with_contact_info.read())["locations"]

    content = {"title": title, "locations": locations}
    return render(request, "mainapp/contact.html", content)
