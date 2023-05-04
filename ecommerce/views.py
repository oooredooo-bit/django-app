from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404

# Create your views here.
def index(request: HttpRequest):
    return render(request, "ecommerce/index.html")

def about(request: HttpRequest):
    return render(request, "ecommerce/about.html")

def handler404(request, exception):
    # raise Http404('Page not found')
    return render(request, 'ecommerce/404.html', status=404)