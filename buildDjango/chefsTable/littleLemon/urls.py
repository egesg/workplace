from django.urls import path
from . import path # dot (.) here indicates the same working directory as the file
from . import views
from django.urls import views

urlpatterns = [
    path("". views.home),
]
