from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ContactUs
from .Serializer import ContactUsSerializer


class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
