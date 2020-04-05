from django.shortcuts import render, redirect
from calls.models import Call, Callee
from datetime import datetime


def index(request):
    call_list = Call.objects.filter(caller=request.user).order_by('-created_at')
    callee_list = Callee.objects.filter(owner=request.user.id)

    has_calls = False
    if call_list:
        has_calls = True

    context = {
        'call_list': call_list,
        'callee_list': callee_list,
        'has_calls': has_calls
    }

    return render(request, 'calls/index.html', context)


def search(request):
    call_list = Call.objects.order_by('-created_at')
    callee_list = Callee.objects.filter(owner=request.user.id)

    if 'callee_id' in request.GET:
        callee_id = request.GET['callee_id']
        if callee_id != "NULL":
            call_list = call_list.filter(callee_id=callee_id)

    if 'start_date' in request.GET:
        start_date = request.GET['start_date']
        if start_date:
            parsed_date = datetime.strptime(start_date, "%m/%d/%Y")
            call_list = call_list.filter(created_at__gte=parsed_date)

    if 'end_date' in request.GET:
        end_date = request.GET['end_date']
        if end_date:
            parsed_date = datetime.strptime(end_date, "%m/%d/%Y")
            call_list = call_list.filter(created_at__lte=parsed_date)

    has_calls = False
    if call_list:
        has_calls = True

    context = {
        'call_list': call_list,
        'callee_list': callee_list,
        'has_calls': has_calls,
        'values': request.GET
    }

    return render(request, 'calls/index.html', context)


def add(request):
    caller = request.user
    callee_id = request.GET['callee_id']
    notes = request.GET['notes']

    callee = Callee.objects.get(id=callee_id)

    new_call = Call(caller=caller, callee=callee, notes=notes)
    new_call.save()

    return redirect('index')


def remove(request, call_id):
    call = Call.objects.filter(id=call_id)
    call.delete()
    return redirect('index')
