from django.shortcuts import render

# Create your views here.
from . import models

# Create your views here.
def index(request):
    pelouses = models.Pelouse_care
    return render(request, 'index.html', locals())
