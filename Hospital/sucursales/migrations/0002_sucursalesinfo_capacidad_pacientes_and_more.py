# Generated by Django 4.2.7 on 2023-11-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursalesinfo',
            name='capacidad_pacientes',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sucursalesinfo',
            name='nombre_sucursal',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='sucursalesinfo',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sucursalesinfo',
            name='ubicacion',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
