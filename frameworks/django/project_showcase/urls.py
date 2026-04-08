from django.contrib import admin
from django.urls import path
from adapters.web import showcase

urlpatterns = [
    path('showcase', showcase.showcase, name='project_showcase'),
]
