from django.db import models

# Create your models here.
class Registrations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_time = models.DateTimeField(auto_now_add=True)