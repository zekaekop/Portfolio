from .models import Anon

class SaveIpAddr:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        ip_addr = self.get_client_ip(request)
        anon, created = Anon.objects.get_or_create(ip_addr=ip_addr)

        if created:
            print("created")
        else:
            print("exists")

        response = self.get_response(request)

        return response 

    def get_client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
