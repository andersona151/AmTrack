from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the AMTS home.")


def dashboard(request):
    return render(request, 'base.html', {'beast': 'austin', } )


def login(request):
    return render(request, 'login.html', {})




