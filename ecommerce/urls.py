from django.urls import path
from ecommerce import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("gallery", views.gallery, name="gallery"),
    path("contact", views.contact, name="contact")
]