# Generated by Django 2.0.2 on 2018-12-26 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_corte_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corte',
            name='sucursal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_sucursales', to='admin_app.Sucursal', verbose_name='Sucursal'),
        ),
    ]
