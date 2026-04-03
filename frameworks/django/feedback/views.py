from django.shortcuts import render
from adapters.persistence.models import Anon
from .models import Feedback
from frameworks.django.home.views import get_client_ip

# Create your views here.
def report(request):

    if request.method == "POST":
        Feedback.objects.create(
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            anon=Anon.objects.get(ip_addr=get_client_ip(request)),
        )
    
    content = {
        "test":"test",
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "feedback/feedback_form.html" , content)