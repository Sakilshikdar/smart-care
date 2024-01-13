from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Service
from .Serializer import ServiceSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
