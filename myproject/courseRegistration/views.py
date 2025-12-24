from django.shortcuts import render
import json
from django.http import JsonResponse
from courseRegistration.models import Registrations
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def createRegistration(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            Registrations.objects.create(
                name = data["name"],
                email = data["email"],
                course = data["course"],
                phone = data["phone"]
            )
            return JsonResponse({
                'status':'success',
                'message':'Data is Created Successfully',
                'data':data
            },status = 201)
        return JsonResponse({
            'Status':'Failed',
            'message':'Check Your Request Method'
        },status = 500)
        
    except Exception as e:
        return JsonResponse({
            'Status':'Error',
            'message':str(e)
        },status = 500)        


def getRegistrations(request):
    try:
        if request.method == 'GET':
            details = Registrations.objects.all().values()
            return JsonResponse({
                'status':'Success',
                'message':'Data retrived Sucessfully',
                'data': list(details)
            },status = 200)
        return JsonResponse({
            'status':'Failed',
            'message':'Check Your Method'
        },status = 500)
    except Exception as e:
        return JsonResponse({
            'status':'Error',
            'message':str(e)
        },status = 500)    