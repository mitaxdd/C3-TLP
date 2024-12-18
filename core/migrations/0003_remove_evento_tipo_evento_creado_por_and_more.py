# Generated by Django 4.2.13 on 2024-11-25 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='tipo',
        ),
        migrations.AddField(
            model_name='evento',
            name='creado_por',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_evento',
            field=models.CharField(choices=[('INICIO_SEMESTRE', 'Inicio de Semestre'), ('FIN_SEMESTRE', 'Fin de Semestre'), ('INICIO_INSCRIPCION', 'Inicio de Inscripción de Asignaturas'), ('FIN_INSCRIPCION', 'Fin de Inscripción de Asignaturas'), ('RECESO_ACADEMICO', 'Receso Académico'), ('FERIADO_NACIONAL', 'Feriado Nacional'), ('FERIADO_REGIONAL', 'Feriado Regional'), ('INICIO_PLAZOS_SOLICITUDES', 'Inicio de Plazos de Solicitudes Administrativas'), ('FIN_PLAZOS_SOLICITUDES', 'Fin de Plazos de Solicitudes Administrativas'), ('INICIO_PLAZOS_BENEFICIOS', 'Inicio de Plazos para la Gestión de Beneficios'), ('FIN_PLAZOS_BENEFICIOS', 'Fin de Plazos para la Gestión de Beneficios'), ('CEREMONIA_TITULACION', 'Ceremonia de Titulación o Graduación'), ('REUNION_CONSEJO', 'Reunión de Consejo Académico'), ('TALLERES_CHARLAS', 'Talleres y Charlas'), ('DIA_ORIENTACION', 'Día de Orientación para Nuevos Estudiantes'), ('EVENTOS_EXTRACURRICULARES', 'Eventos Extracurriculares'), ('INICIO_CLASES', 'Inicio de Clases'), ('FIN_CLASES', 'Último Día de Clases'), ('DIA_PUERTAS_ABIERTAS', 'Día de Puertas Abiertas'), ('SUSPENSION_COMPLETA', 'Suspensión de Actividades Completa'), ('SUSPENSION_PARCIAL', 'Suspensión de Actividades Parcial')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
