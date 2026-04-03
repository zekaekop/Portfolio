from django.shortcuts import render
from adapters.persistence.models import Anon, Feedback
from adapters.persistence import repositories
from frameworks.django.home.views import get_client_ip

from use_cases import use_cases

from django.conf import settings

def get_repositories() -> dict:
    return {"feedback_repository":repositories.DjangoFeedbackRepository()}

# Create your views here.

# This is temporary i will in the future implement feedback with Githubs REST API for issues. 
# Ideas: i could make a bot, that creates issues based on feedback reports so people dont have to make an account
# https://docs.github.com/en/rest/issues/issues?apiVersion=2026-03-10#create-an-issue
def feedback_report(request):

    if request.POST:
        use_cases.create_feedback_report(
            repository=get_repositories()[settings.FEEDBACK_REPOSITORY],
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            anon=Anon.objects.get(ip_addr=get_client_ip(request)),
        )
    
    content = {
        "test":"test",
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "feedback/feedback_form.html" , content)