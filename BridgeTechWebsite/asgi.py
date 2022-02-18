"""
ASGI config for BridgeTechWebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django import http
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BridgeTechWebsite.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application()
})

