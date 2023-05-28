from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'Asteroid_app_1/index.html')


def about_this_site(request):
  #return HttpResponse('<h1>Hello</h1>')
  return render(request, 'Asteroid_app_1/about_this_site.html')

def get_info(request, get_info):
  return HttpResponse(f'N: {get_info + 1} = {get_info} + {1}')