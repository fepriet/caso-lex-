# Generated by Django 4.0.5 on 2022-06-22 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_solicitudservicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='tecnico_juridico',
        ),
        migrations.AddField(
            model_name='contrato',
            name='nombre_contrato',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='causa',
            name='contrato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contrato'),
        ),
    ]
