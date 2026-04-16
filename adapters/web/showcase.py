from django.shortcuts import render, Http404
from adapters.persistence.models import Anon, Projects
from adapters.persistence import repositories
from django.conf import settings
from frameworks.django.home.views import get_client_ip
from adapters.persistence.applications.project_showcase_service import ProjectActions
from datetime import datetime

def get_repositories() -> dict:
    return {"showcase_repository":repositories.DjangoProjectShowcaseRepository()}

def showcase(request):

    content = {
        "projects":Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase.html" , content)

def create_project_card(request):

    create_status = False

    # project_card_data = request.POST or {}
    # if project_card_data:
    #     raise Http404("Could not get showcase card creation post data")

    data = {}
    
    if request.method == "POST":

        data = { 
            "title":request.POST.get("title"),
            "desc":request.POST.get("description"),
            "uploaded_date":datetime.now(),
            "image":request.FILES.get("image"),
            "github_url":request.POST.get("github_url"),
            # "anon":Anon.objects.get(ip_addr=get_client_ip(request)),
        }

        create_status = ProjectActions().create_project_showcase_card(data)
    
    content = {
        "projects":Projects.objects.all(),
        "create_status": create_status,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase_project_create.html" , content)

