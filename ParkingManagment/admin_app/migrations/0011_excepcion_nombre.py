# Generated by Django 2.0.2 on 2019-02-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0010_excepcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='excepcion',
            name='nombre',
            field=models.CharField(default='Rodrigo', max_length=200, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
