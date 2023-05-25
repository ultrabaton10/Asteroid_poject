from django.shortcuts import render


def index(request):
    return render(request, 'Asteroid_app_1/index.html')
