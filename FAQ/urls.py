from django.urls import path, reverse
from . import views

app_name = 'FAQ'

FAQCards = views.FAQCards()
FAQSubmissions = views.FAQSubmissions()

urlpatterns = [
    path('answers/', FAQCards.list_FAQ , name="answers"),
    path('submissions/', FAQSubmissions.list_submissions , name="submissions"),
]