# Generated by Django 4.2.13 on 2024-11-25 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_evento_tipo_evento_creado_por_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Evento',
        ),
    ]
