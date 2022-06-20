# Generated by Django 4.0.5 on 2022-06-20 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cliente_comuna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abogado',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='tecnicojuridico',
            name='usuario',
        ),
        migrations.AddField(
            model_name='cliente',
            name='is_abogado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='is_tecnico',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='abogado',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del Abogado'),
        ),
    ]
