from django.urls import path
from ecommerce import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("gallery", views.gallery, name="gallery"),
    path("contact", views.contact, name="contact"),

    # product urls
    # or better if you create a separate app for product
    path('product/create/', views.create_product, name='create_product'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/update/<int:pk>/', views.update_product, name='update_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),
]