# """geekshop URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import include, path

# # import mainapp.views as mainapp
# from mainapp.views import *

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("mainapp.urls")),
# ]


# from django.conf import settings
# from django.conf.urls import include
# from django.conf.urls.static import static
# from django.urls import path

# import mainapp.views as mainapp

# # from mainapp.views import *

# urlpatterns = [
#     path("", mainapp.MainPage.as_view(), name="main"),
#     path("products/", include("mainapp.urls", namespace="products")),
#     path("contact/", mainapp.Contact.as_view(), name="contact"),
#     path("auth/", include("authnapp.urls", namespace="auth")),
#     path("basket/", include("basketapp.urls", namespace="basket")),
#     path("admin/", include("adminapp.urls", namespace="admin")),
# ]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.MainPage.as_view(), name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.Contact.as_view(), name="contact"),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
