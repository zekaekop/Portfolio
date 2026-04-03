from adapters.persistence.models import Anon
from adapters.persistence import repositories
from django.conf import settings

class SaveIpAddr:

    def __init__(self, get_response):

        self.get_response = get_response
    
    def get_repositories(self) -> dict:
        return {"faq_repository":repositories.DjangoFAQRepository()}

    def __call__(self, request):

        ip_addr = self.get_client_ip(request)
        created = self.get_repositories()[settings.FAQ_REPOSITORY].get_or_create_anon(ip_addr)

        print("new IP ADDR created " + ip_addr) if created else print("IP ADDR exists " + ip_addr)

        response = self.get_response(request)

        return response 

    def get_client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
