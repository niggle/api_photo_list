# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-01 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoupload',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
