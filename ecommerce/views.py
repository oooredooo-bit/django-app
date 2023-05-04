from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

# Create your views here.
def index(request: HttpRequest):
    return render(request, "ecommerce/index.html")

def about(request: HttpRequest):
    return render(request, "ecommerce/about.html")

def gallery(request: HttpRequest):
    return render(request, "ecommerce/gallery.html")

def contact(request: HttpRequest):
    return render(request, "ecommerce/contact.html")