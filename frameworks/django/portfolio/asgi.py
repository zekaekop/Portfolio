"""
ASGI config for portfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

# Note: this ordering is apperantly very important, i need to remember this

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frameworks.django.portfolio.settings')

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

from frameworks.django.account.user_status_consumer import UserStatusConsumer



application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter([path('ws/status/', UserStatusConsumer.as_asgi()),]),
    )
})