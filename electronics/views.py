from django.shortcuts import render
from .models import product

def gadjets(request):
    mobResponse=product.objects.all()
    print(mobResponse)
    return render(request,'blogs/allblogs.html',{'gadjets':mobResponse})
def read(request,id):
    mobResponse=product.objects.get(id=id)
    return render(request,'blogs/readblog.html',{'read':mobResponse}) 
def home(request):
    return render(request,'blogs/home.html')     


# Create your views here.
