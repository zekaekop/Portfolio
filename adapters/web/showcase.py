from django.shortcuts import render, Http404
from adapters.persistence.models import Anon, Projects
from adapters.persistence import repositories
from django.conf import settings
from frameworks.django.home.views import get_client_ip
from adapters.persistence.applications.project_showcase_service import ProjectActions
from datetime import datetime
from django.core.paginator import Paginator

def get_repositories() -> dict:
    return {"showcase_repository":repositories.DjangoProjectShowcaseRepository()}

def paginate_data(request, data, amount):
    # Paginate users by 30 per page, this is an example
    paginator = Paginator(data, amount)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return page_obj

def showcase(request):
    projects = Projects.objects.all()

    page_obj = paginate_data(request, projects, 6)

    content = {
        "projects": page_obj,
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
        "create_status": create_status,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "project_showcase/showcase_project_create.html" , content)
