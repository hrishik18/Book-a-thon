from django import views
from django.contrib import admin
from django.urls import include
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("collection/", views.collection, name="collection"),
]
