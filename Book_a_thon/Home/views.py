from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'main.html')

def collection(request):
    return render(request,'collection.html')

def display(request):
    return render(request,'display.html')

