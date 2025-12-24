"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic.views import createProduct,home,about,contact,menu,details,hello,productInfo,filteringData,filterStudentByCity,pagination,createEmployee 
from newapp.views import orderPlacing,bookmyshow
from courseRegistration.views import createRegistration,getRegistrations
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('menu/',menu,name='menu'),
    path('details/',details),
    path('hello/',hello),
    path('product/',productInfo),
    path('filter/',filteringData),
    path('filterbycity/',filterStudentByCity),
    path('pagination/',pagination),
    path('emp/',createEmployee),
    path('createproduct/',createProduct),
    path('orderplacing/',orderPlacing),
    path('bookmyshow/',bookmyshow),
    path('registration/',createRegistration),
    path('registrationdetails/',getRegistrations)
]
