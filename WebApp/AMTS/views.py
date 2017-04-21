from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from datetime import datetime
from .scripts.time_calcs import *


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
def map_markers(request):
    req_data = request.POST
    # Gather parameters for the range data.
    start_date = req_data['start_date']
    end_date = req_data['end_date']
    machine_id = req_data['machine_id']

    # TODO: Declare the latitude & longitude -- STUCK
    latitude = []
    longitude = []

    # Gather the latitudes based off above parameters
    lat_range_data = Machine.objects.filter(CollectionTime__range=[start_date, end_date]) \
        .filter(machine_uid=machine_id) \
        .filter(latitude=latitude)

    # Gather the longitudes based off above parameters
    lon_range_data = Machine.objects.filter(CollectionTime__range=[start_date, end_date]) \
        .filter(machine_uid=machine_id) \
        .filter(longitude=longitude)

    # TODO: Send off the longitude & latitude lists -- FIX
    data = {'longitude': lat_range_data,
            'latitude': lon_range_data}
    return JsonResponse(data)


@login_required
@csrf_exempt
def machine_search(request):
    req_data = request.POST
    start_date = req_data['start_date']
    end_date = req_data['end_date']
    machine_id = req_data['machine_id']
    start_date = datetime.strptime(start_date, '%m/%d/%Y')
    end_date = datetime.strptime(end_date, '%m/%d/%Y')

    range_data = Machine.objects.filter(CollectionTime__range=[start_date, end_date]).filter(machine_uid=machine_id)
    range_data_idle = Machine.objects.filter(CollectionTime__range=[start_date, end_date]) \
        .filter(machine_uid=machine_id) \
        .filter(idle=True)
    range_data_not_idle = Machine.objects.filter(CollectionTime__range=[start_date, end_date]) \
        .filter(machine_uid=machine_id) \
        .filter(idle=False)

    dist = distance_traveled(range_data)
    total_time = get_total_time(start_date, end_date)  # THIS IS A TUPLE [days, hours]
    time_on = get_time_on(range_data)  # THIS IS A TUPLE [days, hours]
    time_idle = get_time_idle(range_data_idle)  # THIS IS A TUPLE [days, hours]
    time_off = get_time_off(time_on, total_time)  # THIS IS A TUPLE [days, hours]
    avg_speed = get_average_speed(range_data_not_idle)
    data = {'distance': dist,
            'total_time': total_time,
            'time_on': time_on,
            "time_idle": time_idle,
            'time_off': time_off,
            'avg_speed': avg_speed}
    return JsonResponse(data)
