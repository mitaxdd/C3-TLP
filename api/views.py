from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento
from .serializers import EventoSerializer
from .request import obtener_feriados
from .permisos import IsAdminOrReadOnly

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAdminOrReadOnly]

#json con formato para consumo (interno) de la api para fullcalendarjs
def get_eventos_fcjs(request):
    events = list(Evento.objects.values('title', 'start', 'end'))

    calendarific_events = obtener_feriados()

    combined_events = events + calendarific_events
    
    return JsonResponse(combined_events, safe=False)

#json con formato para consumo externo de la api
def get_eventos(request):

    events = list(Evento.objects.values())

    calendarific_events = obtener_feriados()

    combined_events = events + calendarific_events
    
    return JsonResponse(combined_events, safe=False)