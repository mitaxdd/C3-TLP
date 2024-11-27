from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, get_eventos

router = DefaultRouter()
router.register('eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/eventos/', get_eventos, name='get_eventos'),
]