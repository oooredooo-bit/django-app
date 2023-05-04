from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, "ecommerce/index.html")

def about(request: HttpRequest):
    return render(request, "ecommerce/about.html")