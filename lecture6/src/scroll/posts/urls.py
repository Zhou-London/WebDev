from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path("", views.index),
    path("posts", views.posts, name="posts"),
    path("APIs", views.APIs, name="APIs")
]