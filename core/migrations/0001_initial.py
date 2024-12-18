# Generated by Django 4.2.13 on 2024-11-19 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('nombre', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('profesor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asignatura')),
            ],
        ),
    ]
