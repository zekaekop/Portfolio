from django.contrib import admin
from django.urls import path
from adapters.web import showcase

app_name="project_showcase"

urlpatterns = [
    path('showcase', showcase.showcase, name='project_showcase'),
    path('create', showcase.create_project_card, name='create_project_card'),
]
