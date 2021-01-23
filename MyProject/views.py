from django.shortcuts import render

from . import settings
import os

# Create your views here.

def index(request):
    print(os.environ['DEBUG_KEY'])
    print("Secret Key",os.environ.get('SECRET_KEY'))
    return render(request, 'index.html')
