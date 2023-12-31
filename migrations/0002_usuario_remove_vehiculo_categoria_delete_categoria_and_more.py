# Generated by Django 4.2.2 on 2023-11-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut')),
                ('nombre', models.CharField(max_length=80, verbose_name='nombre')),
                ('apellido', models.CharField(blank=True, max_length=80, null=True, verbose_name='apellido')),
                ('tipo_de_usuario', models.CharField(choices=[('Secretaria', 'Secretaria'), ('Cajero', 'Cajero'), ('Medico', 'Medico'), ('Paciente', 'Paciente')], max_length=40, verbose_name='tipo de usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
