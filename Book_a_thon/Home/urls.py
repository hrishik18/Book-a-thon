from django import views
from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.main, name='main'),
    path("collection/", views.collection, name='collection'),
    path("saved/", views.main, name='saved')
]
