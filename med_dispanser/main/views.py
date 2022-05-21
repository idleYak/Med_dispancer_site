from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Symbol, Service, Receipt, Talon
from django.views.generic.list import ListView
from django.core.cache import cache
from django.http import HttpResponse
from datetime import datetime
import logging

def timing(request):
    receipt = Receipt.objects.all()
    if request.method == 'POST':
        if request.POST['id_t'] == 'Back':
            return redirect(index)
        id_time = request.POST['id_t']
        cache.set('id_time', id_time)
        return redirect(talon)
    return render(request, 'main/timing.html', {'receipt': receipt})

def index(request):
    service = Service.objects.all()
    if request.method == 'POST':
        id_serv = request.POST['id']
        cache.set('id_serv', id_serv)
        return redirect(timing)
    return render(request, 'main/index.html', {'service': service})


def doc(request):
    #logger.error("Testing")   # вот он
    if request.method == 'GET':
        id_tal = cache.get('id_tal')
        id_serv = cache.get('id_serv')
        id_time = cache.get('id_time')
        service = Service.objects.get(id=id_serv)
        receipt = Receipt.objects.get(id=id_time)
        talon = Talon.objects.get(id=id_tal)
        cache.delete_many(['id_tal', 'id_serv', 'id_time'])
    return render(request, 'main/doc.html', {'talon': talon, 'service': service, 'receipt': receipt})


def talon(request):
    if request.method == 'POST':
        id_tal = int(request.POST['id'])
        if id_tal == 1:
            id_serv = cache.get('id_serv')
            id_time = cache.get('id_time')
            service = Service.objects.get(id=id_serv)
            receipt = Receipt.objects.get(id=id_time)
            tal = Talon(id_service=service, id_time_of_receipt=receipt, condition=0,
                        time_registration=datetime.now().time())
            tal.save()
            cache.set('id_tal', tal.id)
            return redirect(doc)
        if id_tal == 2:
            return redirect(timing)
    return render(request, 'main/talon.html')


def helper(request):
    return render(request, 'main/helper.html')

def printer(request):
    return render(request, 'main/index.html')
