from django.shortcuts import render
from .models import shopping, shopping1
def Men(request):
    mobResponse=shopping.objects.all()
    print(mobResponse)
    return render(request,'blogs1/allblogs1.html',{'Men':mobResponse})
def Women(request):
    mobResponse=shopping1.objects.all()
    return render(request,'blogs1/readblog1.html',{'Women':mobResponse})    
def read(request,id):
    mobResponse=shopping.objects.get(id=id)
    return render(request,'blogs1/readblog2.html',{'read':mobResponse}) 
def read1(request,id):
    mobResponse=shopping1.objects.get(id=id)
    return render(request,'blogs1/readblog3.html',{'read1':mobResponse})    
# Create your views here.
