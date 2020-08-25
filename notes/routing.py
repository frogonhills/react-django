from django.urls import path 

from . import consumers

websocket_urlpatterns = [
  path('notes', consumers.NoteConsumer)
]