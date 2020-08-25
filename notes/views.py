from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers


# Create your views here.



class NoteList(generics.ListCreateAPIView):          #generics.ListAPIView use korle shudhu dekha jabe create or delete kora jabe na 
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer



class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer