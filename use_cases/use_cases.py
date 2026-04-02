from django.shortcuts import render
from adapters.persistance.models import FAQuestions, FAQuestionsSubmissions
from adapters.persistance.account import Anon
from frameworks.django.home.views import get_client_ip
from core import entities
# Create your views here.

def create_FAQ(
    repository: interfaces.FAQRepository,
    anon: int,
    asked_question: str,
    answer: str,
    ):
    
    faq = entities.FAQ(
        anon = request.POST.get(ip_addr=get_client_ip(request)),
        asked_question = request.POST.get("asked_question"),
        answer = request.POST.get("answer"),
    )

    # why not just add the POST data directly into faq_dict?
    faq_dict = dict(
        anon = faq.anon,
        asked_question = faq.asked_question,
        answer = faq.answer
    )

    repository.create(faq_dict)

        
        