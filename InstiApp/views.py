from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import RegisterClasses
from .serializers import RegisterSerializer
from .forms import PostForm

# Create your views here.

class RegisterClassesViewSet(viewsets.ModelViewSet):
    queryset = RegisterClasses.objects.all()
    serializer_class = RegisterSerializer

def Indexing(request):
    return HttpResponse('<center><h1>Welcome to the django Back-End Environment</h1></center><hr/><br/><center><h3>Here will appear the datas of the uers from your project</h3><br/><br/><img src="https://maxmautner.com/public/images/django.gif" alt="django"/></center>')