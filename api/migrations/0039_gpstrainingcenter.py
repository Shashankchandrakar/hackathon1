# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_delete_gpstrainingcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpsTrainingCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtc_name', models.CharField(max_length=255)),
                ('gtc_lat', models.FloatField(blank=True, default=None, null=True)),
                ('gtc_lon', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]