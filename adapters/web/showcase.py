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
        "test":"test",
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase_project_create.html" , content)

