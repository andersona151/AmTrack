from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout


def home(request):
    return HttpResponse("Hello, world. You're at the AMTS home.")


def dashboard(request):
    return render(request, 'base.html', {'beast': 'austin'})


def login_page(request):
    return render(request, 'login.html', {"Title": "Ameritrack Equipment Utilization Tracking", })


@login_required
def reports(request):
    return render(request, 'reports.html', {"Title": "Ameritrack Equipment Utilization Tracking", })


def login(request):
    if request.user.is_authenticated():
        return redirect('reports')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            return redirect('reports')

    return render(request, 'login.html', {'next': request.GET.get('next'),
                                          "Title": "Ameritrack Equipment Utilization Tracking",
                                          })


def logout_view(request):
    logout(request)
    return redirect('login')
