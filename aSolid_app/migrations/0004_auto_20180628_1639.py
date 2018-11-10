# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aSolid_app', '0003_auto_20180627_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='aSolid_app.Quote'),
        ),
    ]
