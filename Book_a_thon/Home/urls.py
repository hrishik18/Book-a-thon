from django import views
from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("display/", views.display, name='display'),
    path("collection/", views.collection, name='collection'),
]
