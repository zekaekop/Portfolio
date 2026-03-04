from django.urls import path, reverse
from . import views

app_name = 'feedback'

urlpatterns = [
    path('report/', views.report , name="report"),
]