from django.shortcuts import render
from django.http import HttpRequest
from django.apps import apps
from .forms import ContactForm

# Getting application config
app_config = apps.get_app_config(__name__.split('.')[0])
app_name = app_config.name

# Create your views here.
def index(request: HttpRequest):
    return render(request, f"{app_name}/index.html")

def about(request: HttpRequest):
    return render(request, f"{app_name}/about.html")

def gallery(request: HttpRequest):
    return render(request, f"{app_name}/gallery.html")

# def contact(request: HttpRequest):
#     return render(request, f"{app_name}/contact.html")

def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, f'{app_name}/thank_you.html')
    else:
        form = ContactForm()

    return render(request, f'{app_name}/contact.html', {'form': form})