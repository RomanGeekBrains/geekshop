# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path

# from .views import *

# urlpatterns = [
#     path("", main, name="home"),
#     path("products/", products, name="products"),
#     path("products/all", products, name="products_all"),
#     path("products/home", products, name="products_home"),
#     path("products/office", products, name="products_office"),
#     path("products/modern", products, name="products_modern"),
#     path("products/classic", products, name="products_classic"),
#     path("contact/", contact, name="contact"),
# ]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("<int:pk>/", mainapp.products, name="category"),
]
