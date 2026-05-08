from django import http
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import Http404, render
from django.core.paginator import Paginator
# # del ts all
# from adapters.persistence.models import GenericQueries

from frameworks.django.home.views import get_client_ip

from adapters.persistence import repositories, models
from use_cases import use_cases

def get_repositories() -> dict:
    return {"faq_repository":repositories.DjangoFAQRepository()}

def paginate_data(request, data, amount):
    # Paginate users by 30 per page, this is an example
    paginator = Paginator(data, amount)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return page_obj

def create_FAQ(request):
     
    # this is a cleaner way to write if request.method == "POST" and store data
    faq_data = request.POST or {}
    if not faq_data:
        raise Http404("Frequently asked question does not have POST data.")
    
    use_cases.create_FAQ(
        repository = get_repositories()[settings.FAQ_REPOSITORY],
        anon = models.Anon.objects.get(ip_addr=get_client_ip(request)),
        question = faq_data.get("question"),
        answer = faq_data.get("answer"),
        desc = faq_data.get("desc"),
    )

def answer_FAQ(request):
     
    # this is a cleaner way to write if request.method == "POST" and store data
    faq_answer_data = request.POST or {}
    if not faq_answer_data:
        raise Http404("Frequently asked question does not have POST data.")
    
    use_cases.answer(
        repository = get_repositories()[settings.FAQ_REPOSITORY],
        anon = models.Anon.objects.get(ip_addr=get_client_ip(request)),
        question = faq_answer_data.get("question"),
        answer = faq_answer_data.get("answer"),
        desc = faq_answer_data.get("desc"),
    )

def dashboard(request):
    faqs = list_FAQ(request)

    questions = paginate_data(request, faqs, 4)
    
    if request.POST:
        create_FAQ(request)

    content = {
       # "ip_addr":get_client_ip(request),
        "FAQs": questions,
    }

    return render(request, "FAQ/FAQ.html", content)

def list_FAQ(request):
    return repositories.DjangoFAQRepository().list()

def archive_FAQ(request):
    use_cases.archive_FAQ(request.POST.get("archive_id"))
    GenericQueries.list(request)