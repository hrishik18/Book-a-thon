from django import views
from django.contrib import admin
from django.urls import path, include
#from django.config.urls import url
from Home import views

urlpatterns = [
    path("", views.main, name='main'),
    path("collection/", views.collection, name='collection'),
    path("display/", views.display, name='display'),
    path("saved/", views.addbook, name='saved'),
    path("#<slug:slug>",views.addbook,name="saved")
]
