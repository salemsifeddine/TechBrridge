from django.urls import  path
from .Consumers import WSConsumer

ws_urlpatterns=[
    path("ws/someurl/",WSConsumer.as_asgi())
]