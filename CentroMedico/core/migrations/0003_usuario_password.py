# Generated by Django 4.2.2 on 2023-11-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_remove_vehiculo_categoria_delete_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='contraseña', max_length=128),
        ),
    ]