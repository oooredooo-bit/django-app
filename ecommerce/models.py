from django.db import models

# Create your models here.
class Inquiries(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    message = models.TextField()