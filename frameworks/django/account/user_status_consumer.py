
from channels.generic.websocket import WebsocketConsumer
from adapters.persistence.models import Anon

class UserStatusConsumer(WebsocketConsumer):
    def connect(self):
        print("connected", event)   
        user = self.scope['user']
        self.update_user_status(user, 'online')

    
    def disconnect(self, close_code):
        print("disconnected", event)
        user = self.scope['user']
        self.update_user_status(user, 'online')

    # default is 0 for offline and 1 for online
    def apply_user_status(user, status=0):
        return Anon.objects.filter(pk=user.pk).update(status=status)