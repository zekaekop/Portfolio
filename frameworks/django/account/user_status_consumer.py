
from channels.generic.websocket import WebsocketConsumer
from adapters.persistence.models import Anon, UserProfile
from frameworks.django.account import middlewares

class UserStatusConsumer(WebsocketConsumer):
    def connect(self):

        # Scope user does not exist??
        # Note: Apperantly scope user is predefined
        self.user = self.scope.get('user')

        if (self.user.is_authenticated):
            user = self.user
            self.apply_user_status(UserProfile , user, 1)
        else:
            ip_addr =  self.get_client_ip()
            user = Anon.objects.get_or_create(ip_addr=ip_addr)
            self.apply_user_status(Anon , user, 1)

        self.accept()

    
    def disconnect(self, close_code):

        if (self.user.is_authenticated):
            user = self.user
            self.apply_user_status(UserProfile , user, 0)
        else:
            ip_addr =  self.get_client_ip()
            user = Anon.objects.get(ip_addr=ip_addr)
            self.apply_user_status(Anon , user, 0)

    # default is 0 for offline and 1 for online
    # Its wastefull to store "online" and "offline" as str
    def apply_user_status(self, model, user, status=0):
        return model.objects.filter(pk=user.pk).update(activity_status=status)

    # Aperrantly i need this code, since i cannot pass request through websockets, to run middleware to get ip_addr
    def get_client_ip(self):
        """Extract client IP from scope"""
        # Try x-forwarded-for header first (for proxies)
        headers = dict(self.scope.get('headers', []))
        if b'x-forwarded-for' in headers:
            ip = headers[b'x-forwarded-for'].decode().split(',')[0]
            return ip
        
        # Fall back to client address
        client = self.scope.get('client')
        if client:
            return client[0]
        
        return '0.0.0.0'