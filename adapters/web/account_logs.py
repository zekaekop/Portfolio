from django.shortcuts import render
from adapters.persistence.models import Log, Anon

# Create your views here.

def list_user_logs(request):

    content = {
        "logs": Log.objects.get(user_id=request.pk).all(),
        "ip_addr": Anon.objects.get(ip_addr=get_client_ip(request)).ip_addr,
    }
    
    return render(request, "account/logs.html" , content)