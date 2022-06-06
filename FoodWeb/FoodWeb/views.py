from django.http import  HttpResponse
from django.shortcuts import render
from django.shortcuts import render

def HomePage(request):
    return render(request,'FoodWeb/HomePage.html')




