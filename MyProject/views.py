from django.shortcuts import render

from . import settings
import os

# Create your views here.

def index(request):
    print(os.environ['DEBUG_VALUE'])
    return render(request, 'index.html')
