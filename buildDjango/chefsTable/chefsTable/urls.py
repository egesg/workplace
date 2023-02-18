"""chefsTable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from littleLemon import views # or from . import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.home, name = "home") ->  works without suffix  -> http://127.0.0.1:8000/home
 
    path("say_hello/", views.say_hello), # works only with suffix -> http://127.0.0.1:8000/say_hello/
    path('homepage/', views.homepage), # works only with suffix -> http://127.0.0.1:8000/homepage/

    path("display_date/", views.display_date),

    path("menu/", views.menu),
]
