from django.shortcuts import render, redirect
from calls.models import Call, Callee
from datetime import datetime


def index(request):
    if request.user.is_authenticated:
        call_list = Call.objects.filter(caller=request.user).order_by('-created_at')
        callee_list = Callee.objects.filter(owner=request.user.id).order_by('name')

        has_calls = False
        if call_list:
            has_calls = True

        context = {
            'call_list': call_list,
            'callee_list': callee_list,
            'has_calls': has_calls
        }

        return render(request, 'calls/index.html', context)
    else:
        return redirect('login')


def rolodex(request):
    callee_list = Callee.objects.filter(owner=request.user.id).order_by('name')

    has_callees = False
    if callee_list:
        has_callees = True

    context = {
        'callee_list': callee_list,
        'has_callees': has_callees
    }

    return render(request, 'calls/rolodex.html', context)


def search(request):
    call_list = Call.objects.order_by('-created_at')
    callee_list = Callee.objects.filter(owner=request.user.id).order_by('name')

    if 'callee_id' in request.GET:
        callee_id = request.GET['callee_id']
        if callee_id != "ALL":
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


def add_call(request):
    caller = request.user
    callee_id = request.GET['callee_id']
    notes = request.GET['notes']

    callee = Callee.objects.get(id=callee_id)

    new_call = Call(caller=caller, callee=callee, notes=notes)
    new_call.save()

    return redirect('index')


def remove_call(request, call_id):
    call = Call.objects.filter(id=call_id)
    call.delete()
    return redirect('index')


def add_callee(request):
    callee_name = request.GET['name']
    new_callee = Callee(name=callee_name, owner=request.user)
    new_callee.save()
    return redirect('rolodex')


def remove_callee(request, callee_id):
    callee = Callee.objects.filter(id=callee_id)
    callee.delete()
    return redirect('rolodex')
