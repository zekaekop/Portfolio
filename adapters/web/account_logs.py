from django.shortcuts import render
from adapters.persistence.models import Log, Anon

# Create your views here.

def list_user_logs(request, user_id):

    content = {
        "logs": Log.objects.filter(user_id=user_id).all(),
        # "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "admin_panel/logs.html" , content)