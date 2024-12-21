from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name="greet"),
    path("zhou/", views.zhou, name = "zhou"),
    path("william/", views.William, name = "william")  
]