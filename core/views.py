from django.shortcuts import render
from django.http import JsonResponse
from api.models import Evento

def index(request):
    return render(request, 'index.html')

def calendar_view(request):
    return render(request, 'calendar.html')