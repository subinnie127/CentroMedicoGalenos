# Generated by Django 4.2.2 on 2023-06-30 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=80, verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=80, verbose_name='Marca vehículo')),
                ('servicio', models.CharField(choices=[('suspension_direccion', 'Suspension y Direccion'), ('cajas_cambio', 'Cajas de Cambio'), ('electronica_automotriz', 'Electronica Automotriz')], max_length=40, verbose_name='servicio')),
                ('detalle_servicio', models.CharField(max_length=200, verbose_name='detalle servicio')),
                ('modelo', models.CharField(blank=True, max_length=80, null=True, verbose_name='Modelo')),
                ('imagen', models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoria')),
            ],
        ),
    ]