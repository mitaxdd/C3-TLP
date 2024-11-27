from django.contrib import admin
from .models import *
from api.models import Evento

# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Examen)
admin.site.register(Actividad)
admin.site.register(Evento)