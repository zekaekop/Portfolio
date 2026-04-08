from django.urls import path, reverse

from adapters.web import FAQ
views = FAQ
app_name = 'FAQ'

urlpatterns = [
    path('answers/', views.list_FAQ , name="answers"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create_FAQ , name="create"),
]