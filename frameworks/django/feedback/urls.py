from django.urls import path, reverse
from adapters.web import feedback

views = feedback

app_name = 'feedback'

urlpatterns = [
    path('report/', views.feedback_report , name="report"),
]