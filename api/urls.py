from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, get_eventos_fcjs, get_eventos

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_eventos_fcjs/', get_eventos_fcjs, name='get_eventos_fcjs'),
    path('get_eventos/', get_eventos, name='get_eventos')
]