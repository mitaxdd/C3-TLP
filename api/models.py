from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    TIPOS_EVENTO = [
        ('INICIO_SEMESTRE', 'Inicio de Semestre'),
        ('FIN_SEMESTRE', 'Fin de Semestre'),
        ('INICIO_INSCRIPCION', 'Inicio de Inscripción de Asignaturas'),
        ('FIN_INSCRIPCION', 'Fin de Inscripción de Asignaturas'),
        ('RECESO_ACADEMICO', 'Receso Académico'),
        ('FERIADO_NACIONAL', 'Feriado Nacional'),
        ('FERIADO_REGIONAL', 'Feriado Regional'),
        ('INICIO_PLAZOS_SOLICITUDES', 'Inicio de Plazos de Solicitudes Administrativas'),
        ('FIN_PLAZOS_SOLICITUDES', 'Fin de Plazos de Solicitudes Administrativas'),
        ('INICIO_PLAZOS_BENEFICIOS', 'Inicio de Plazos para la Gestión de Beneficios'),
        ('FIN_PLAZOS_BENEFICIOS', 'Fin de Plazos para la Gestión de Beneficios'),
        ('CEREMONIA_TITULACION', 'Ceremonia de Titulación o Graduación'),
        ('REUNION_CONSEJO', 'Reunión de Consejo Académico'),
        ('TALLERES_CHARLAS', 'Talleres y Charlas'),
        ('DIA_ORIENTACION', 'Día de Orientación para Nuevos Estudiantes'),
        ('EVENTOS_EXTRACURRICULARES', 'Eventos Extracurriculares'),
        ('INICIO_CLASES', 'Inicio de Clases'),
        ('FIN_CLASES', 'Último Día de Clases'),
        ('DIA_PUERTAS_ABIERTAS', 'Día de Puertas Abiertas'),
        ('SUSPENSION_COMPLETA', 'Suspensión de Actividades Completa'),
        ('SUSPENSION_PARCIAL', 'Suspensión de Actividades Parcial'),
    ]

    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50, choices=TIPOS_EVENTO)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
