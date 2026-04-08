from django.shortcuts import render
from adapters.persistence.models import Anon
from frameworks.django.home.views import get_client_ip

def showcase(request):
    
    content = {
        "test":"test",
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase.html" , content)