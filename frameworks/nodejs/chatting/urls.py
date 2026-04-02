from django.urls import path, reverse
from . import views

app_name = 'chatting'

urlpatterns = [
    path('chat/', views.chat , name="chat"),
    path('api/message', views.save_message , name="save_message"),
]