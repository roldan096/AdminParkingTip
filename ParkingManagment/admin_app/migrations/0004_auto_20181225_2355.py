# Generated by Django 2.0.2 on 2018-12-25 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_auto_20181225_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corte',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Nocturno', 'Nocturno')], max_length=50, verbose_name='Turno'),
        ),
    ]
