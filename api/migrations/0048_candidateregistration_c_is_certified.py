# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_batchinfo_batch_last_date_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateregistration',
            name='c_is_certified',
            field=models.BooleanField(default=False),
        ),
    ]