from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest
from django.apps import apps
from .models import Contact, Product
from .forms import ContactForm, ProductForm

# Getting application config
app_config = apps.get_app_config(__name__.split('.')[0])
app_name = app_config.name

# E-Commerce views here
def index(request: HttpRequest):
    return render(request, f"{app_name}/index.html")

def about(request: HttpRequest):
    return render(request, f"{app_name}/about.html")

def gallery(request: HttpRequest):
    return render(request, f"{app_name}/gallery.html")

def contact(request: HttpRequest):
    return render(request, f"{app_name}/contact.html")

# For reference only. You can follow this
# when exercising forms in Django:
# def contact(request: HttpRequest):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, f'{app_name}/thank_you.html')
#     else:
#         form = ContactForm()
#     return render(request, f'{app_name}/contact.html', {'form': form})

# ========================================================================

# Product views here
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, f'{app_name}/products/create.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, f'{app_name}/products/list.html', {'products': products})

def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Product does not exist.")

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, f'{app_name}/products/update.html', {'form': form, 'product': product})

def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Product does not exist.")
    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, f'{app_name}/products/delete.html', {'product': product})