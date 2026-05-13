from django.shortcuts import render
from adapters.persistence.models import Anon, Projects
from django.contrib.auth.models import User
from frameworks.django.home.views import get_client_ip
from adapters.persistence.applications import site_statistics_service
from django.core.paginator import Paginator

admin_paginate_num = 30

def dashboard(request):

    site_stats = site_statistics_service.set_stats(request)

    content = {
        "type": None,
        "projects": None,
        "site_stats": site_stats,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def projects(request):
    projects = Projects.objects.all()

    page_obj = paginate_data(request, projects, admin_paginate_num)

    content = {
        "type": "projects",
        "datas": page_obj,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def anons(request):
    anons = Anon.objects.all()

    page_obj = paginate_data(request, anons, admin_paginate_num)

    content = {
        "type": "anons",
        "datas": page_obj,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def paginate_data(request, data, amount):
    # Paginate users by 30 per page, this is an example
    paginator = Paginator(data, amount)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return page_obj

def users(request):
    users = User.objects.all()
    page_obj = paginate_data(request, users, admin_paginate_num)

    content = {
        "type": "users",
        "datas":page_obj,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

# def tags(request):

#     content = {
#         "type": "tags",
#         "datas": Projects.objects.all(),
#         "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
#     }
    
#     return render(request, "admin_panel/admin_panel.html" , content)

def moderators(request):
    users = User.objects.all()
    page_obj = paginate_data(request, users, admin_paginate_num)

    content = {
        "type": "moderators",
        "datas": page_obj,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def create_project_menu(request):

    if request.POST:
        pass

    content = {
        "type": "projects",
        "projects": Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)