from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    temoins = models.Temoignages.objects.filter(status=True)
    banners = models.Banner.objects.filter(status=True)
    abouts = models.About.objects.filter(status=True)
    return render(request, 'index.html', locals())


