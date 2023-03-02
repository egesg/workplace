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
    # path("admin/", admin.site.urls),
    # path("", views.home, name = "home") ->  works without suffix  -> http://127.0.0.1:8000/home
    path("say_hello/", views.say_hello), # works only with suffix -> http://127.0.0.1:8000/say_hello/
    path('homepage/', views.homepage), # works only with suffix -> http://127.0.0.1:8000/homepage/
    path("display_date/", views.display_date),
    # examples
    path("home/", views.home, name = "home"), # http://127.0.0.1:8000/home/ -> path prints "/home/" -> path is displayed in the main window of browser and it is the same as the order in which you pressed inside the url patterns list
    path("", views.home, name = "home"), # http://127.0.0.1:8000 -> path prints "/" -> path is displayed in the main window of browser and it is the same as the order in which you pressed inside the url patterns list

    # Week 2-1: Creating Requests and Responses
    path("admin/", admin.site.urls),
    path("menu/", views.menu),


    # Week 2-3: Mapping URLs with Params
    path('dishes/<str:dish>', views.menuitems), # example: dish=pasta


    # Week 2: Exercise: Mapping URLs with Params
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 


    # Week 2: Exercise: Creating URLs and Mapping to Views
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),

]

