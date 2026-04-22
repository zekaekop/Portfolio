from django.shortcuts import render
from adapters.persistence.models import Anon, Projects
from django.contrib.auth.models import User
from frameworks.django.home.views import get_client_ip
from adapters.persistence.applications import site_statistics_service

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

    content = {
        "type": "projects",
        "projects": Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def anons(request):

    content = {
        "type": "anons",
        "datas":Anon.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)


def users(request):

    content = {
        "type": "users",
        "datas":User.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def tags(request):

    content = {
        "type": "tags",
        "projects": Projects.objects.all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/admin_panel.html" , content)

def moderators(request):

    content = {
        "type": "moderators",
        "moderators": Anon.objects.all(),
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