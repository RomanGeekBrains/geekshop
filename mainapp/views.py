import json
from django.shortcuts import render


def main(request):
    title = "домашняя"
    with open('mainapp/data_json/products.json', 'r') as file_with_products:
        products = json.loads(file_with_products.read())['products']

    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_home", "name": "дом"},
        {"href": "products_office", "name": "офис"},
        {"href": "products_modern", "name": "модерн"},
        {"href": "products_classic", "name": "классика"},
    ]

    with open('mainapp/data_json/same_products.json', 'r') as file_with_same_products:
        same_products = json.loads(file_with_same_products.read())['same_products']

    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    
    with open('mainapp/data_json/contact_info.json', 'r') as file_with_contact_info:
        locations = json.loads(file_with_contact_info.read())['locations']

    content = {"title": title,  "locations": locations}
    return render(request, "mainapp/contact.html", content)