from django.urls import path
from .consumers import JokesConsumer

ws_urlpatterns = [
    path('ws/jk/', JokesConsumer.as_asgi())
]