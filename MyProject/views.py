from django.shortcuts import render

from . import settings
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')
