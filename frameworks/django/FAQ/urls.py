from django.urls import path, reverse

from adapters.web import FAQ
views = FAQ
app_name = 'FAQ'

urlpatterns = [
    path('answers/', views.list_FAQ , name="answers"),
    # path('submissions/', views.list_submissions , name="submissions"),
    path('create/', views.create_FAQ , name="create"),
]