from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@csrf_exempt
def machine_search(request):
    req_data = request.POST
    start_date = req_data['start_date']
    end_date = req_data['end_date']
    machine_id = req_data['machine_id']
    # calcs here
    data = {}
    return JsonResponse(data)

