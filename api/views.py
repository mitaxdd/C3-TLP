from rest_framework import viewsets
from django.http import JsonResponse
from .models import Evento
from .serializers import EventoSerializer
from .request import obtener_feriados

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().values('title','start','end')
    print(queryset)
    
    serializer_class = EventoSerializer

def get_eventos(request):
    # Obtener eventos de tu API
    events = list(Evento.objects.values('title', 'start', 'end'))
    
    # Obtener eventos de la API de Calendarific
    calendarific_events = obtener_feriados()
    print("CALENDARIFIC", calendarific_events)
    
    # Combinar ambos conjuntos de eventos
    combined_events = events + calendarific_events
    
    return JsonResponse(combined_events, safe=False)

