from django.shortcuts import render
from django.http import Http404, HttpResponse
# Create your views here.

def index(request):
    return render(request, "singlepage2/index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, max. ",
         "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed Lacinia quam. ",
         "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est. "]

def section(request, num):
    if 1<= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")