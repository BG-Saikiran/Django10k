from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import math
from django.views.decorators.csrf import csrf_exempt
import json
from basic.models import Employee,Product



# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

def hello(request):
    name = request.GET.get('name')
    return HttpResponse(name)

def details(request):
    data = {
        'name':'sai','age':22,'gender':'Male'
    }
    
    return JsonResponse(data)

def productInfo(request):
    product_name = request.GET.get('product','mobile')
    quantity = request.GET.get('quantity',2)
    price = request.GET.get('price',300000)
    data = {'product':product_name,'quantity':quantity,'price':price}
    return JsonResponse(data)


def filteringData(request):
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    gt = int(request.GET.get('num',5))
    greater = []
    for i in data:
        if i > gt:
            greater.append(i)
    return JsonResponse(greater,safe=False)


data = [{'name':'sai','city':'ndl'},{'name':'sai','city':'hyd'},{'name':'sai','city':'hyd'}]
def filterStudentByCity(request):
    filteredStudents = []
    city = request.GET.get("city",'hyd')
    for x in data :
        if x['city'] == city:
            filteredStudents.append(x)
    return JsonResponse(filteredStudents,safe=False)


data = ['apple','banana','watermelon','orange','pinapple','promaganate','banana','apple']
def pagination(request):
    page = int(request.GET.get("page",1))
    limit = int(request.GET.get("limit",1))
    
    total_items = len(data)
    per_page = math.ceil(total_items / limit)

    start = (page-1)*per_page
    end = page + per_page
    res = {
        "status" : "success",
        "page" : page,
        "limit":limit,
        "data": data[start : end]}
    return JsonResponse(res)


@csrf_exempt
def createEmployee(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            Employee.objects.create(emp_name = data.get("name"),emp_salary = data.get("salary"),emp_email = data.get("email")
            )
            print(data)
        return JsonResponse({"status":"success","data":data},status = 201)
    
    except Exception as e:
        return JsonResponse({"status":"error"},status = 500)
    
    
@csrf_exempt
def createProduct(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            price = data.get("pro_price")
            quant = data.get("pro_quantity")
            total_price = price * quant
            Product.objects.create(
                 product_name = data.get("pro_name"),
                 product_price = data.get("pro_price"),
                 product_quantity = data.get("pro_quantity"),
                 product_total_price = total_price
             )   
             
            return JsonResponse({"status":"success","data":data})
        
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)})