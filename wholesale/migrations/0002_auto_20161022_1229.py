# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-22 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]