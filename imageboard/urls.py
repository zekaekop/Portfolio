from django.contrib import admin
from django.urls import path
from . import views

app_name = "imageboard"

urlpatterns = [
    path('posts/', views.list_posts, name='list_posts'),
]
