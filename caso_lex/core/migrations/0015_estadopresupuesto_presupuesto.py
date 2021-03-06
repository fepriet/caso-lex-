# Generated by Django 4.0.5 on 2022-06-26 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_contrato_archivo_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoPresupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estadopresupuesto')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.solicitudservicio')),
            ],
        ),
    ]
