"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from .views import home   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),       
]
