from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main.html")


def collection(request):
    return render(request, "collection.html")
