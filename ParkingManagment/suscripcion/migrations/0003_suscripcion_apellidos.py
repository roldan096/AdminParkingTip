# Generated by Django 2.0.2 on 2019-02-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suscripcion', '0002_suscripcion_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscripcion',
            name='apellidos',
            field=models.CharField(default='', max_length=200, verbose_name='Apellidos'),
        ),
    ]