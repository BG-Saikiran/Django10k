from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_total_price = models.FloatField()
    
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_email = models.EmailField(unique=True)    