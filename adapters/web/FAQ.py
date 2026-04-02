from django import http
from django.conf import settings
from django.shortcuts import Http404

from adapters.persistance import repositories
from use_cases import use_cases

def get_repositories() -> dict:
    return {"faq_repository":repositories.DjangoFAQRepository()}

def create_FAQ(request):
     
    # this is a cleaner way to write if request.method == "POST" and store data
    faq_data = request.POST or {}
    if not faq_data:
        raise Http404("Frequently asked question does not have POST data.")
    
    use_cases.create(
        repository = get_repositories()[settings.FAQ_REPOSITORY],
        anon = faq_data.get(ip_addr=get_client_ip(request)),
        asked_question = faq_data.get("asked_question"),
        answer = faq_data.get("answer")
    )

def list_FAQ():
    task = repositories.list()

def archive_FAQ():
    pass