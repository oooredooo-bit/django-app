from django import forms
from .models import Contact, Product

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_no', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'