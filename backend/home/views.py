from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HomeSerializer
from .models import Home

# Create your views here.

class HomeView(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
