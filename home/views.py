from django.shortcuts import render
from account.models import Anon

# Create your views here.

def home_page(request):

    tags = ("CSS","HTML","JS","C","C++","Python","PHP","TypeScript","Bash","MySQL","GIT","Django", "Nginx", "NodeJS", )

    context = {
        "tags":  tags,
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "home/home.html", context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
