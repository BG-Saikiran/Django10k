from django.db import models
import uuid

# Create your models here.


class OrderDetails(models.Model):
    usermail = models.EmailField(unique=True)
    orderid = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    mode = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    dateandtime = models.DateTimeField(auto_now_add=True)
    currecy = models.CharField(default="INR",max_length=50)
    #UUID - UNIVERSALLY UNIQUE ID
    #uuid1 - generates a random num based on time and mac
    #uuid2 - generates a random by combination of digits and characters
    #uuid3 - generates a random num with comb of username and spl charactrs
    transaction_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
       
    
    
class MovieBooking(models.Model):
    movie_name = models.CharField(max_length=100)
    show_time = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100) 
    dataandtime = models.DateTimeField(auto_now_add = True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)