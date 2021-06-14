# Generated by Django 3.2.4 on 2021-06-13 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MB', '0005_auto_20210611_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='perfil',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='perfil',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 6, 13, 19, 30, 6, 746004)),
        ),
    ]
