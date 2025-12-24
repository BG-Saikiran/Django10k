from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from newapp.models import OrderDetails,MovieBooking

# Create your views here.
@csrf_exempt    
def bookmyshow(request):
    try:
        if request.method == "POST":
            data = request.loads(request.body)
            MovieBooking.objects.create(moviename = data["movie_name"],
                                        showtime = data["show_time"],
                                        screenname = data["screen_name"])
            return JsonResponse({"status":"success","msg":"records inserted successfully"},status = 201)
        
        return JsonResponse({"status":"Failed"},status = 400)
    except Exception as e:
        return JsonResponse({"message": "somting went wrong"},status =500)   
    
    
    
@csrf_exempt
def orderPlacing(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            OrderDetails.objects.create(
                orderid = data["order_id"],
                usermail = data["email"],
                amount = data["amount"],
                mode = data["mode"],
                status = data["status"]
            )
            return JsonResponse({"status":"success"},status = 201)
        
        else:
            return JsonResponse({"error":"only Post method is allowed"},status = 400)    
    except Exception as e:
        return JsonResponse({"error":"something went wrong"},status = 500)
   
        
#{"orderid":"ord1","email":"saikiran@gmil.com","amount":2500.50,"status":"success","mode":"Phonepay"}                