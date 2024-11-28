from rest_framework import serializers
from .models import Evento

#serializer de modelo evento
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['title','start','end']