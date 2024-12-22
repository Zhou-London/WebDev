from django.shortcuts import render
from django.http import *

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def zhou(request):
    return HttpResponse("Hello Zhouzhou!")

def William(request):
    return HttpResponse("Hello William!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })