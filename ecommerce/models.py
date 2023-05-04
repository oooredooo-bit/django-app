from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)