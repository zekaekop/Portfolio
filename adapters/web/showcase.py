from django.shortcuts import render
from adapters.persistence.models import Anon, Projects
from frameworks.django.home.views import get_client_ip

def showcase(request):

    content = {
        "projects":Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase.html" , content)

def create_project_card(request):

    content = {
        # "projects":Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase_project_create.html" , content)

