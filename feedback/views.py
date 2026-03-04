from django.shortcuts import render
from account.models import Anon
from home.views import get_client_ip

# Create your views here.
def report(request):
    
    content = {
        "test":"test",
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "feedback/feedback_form.html" , content)