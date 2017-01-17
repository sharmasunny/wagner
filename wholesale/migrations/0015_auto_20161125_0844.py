# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-25 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0014_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='flowers_names',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='quantity_list',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order_item',
            name='order_list',
            field=models.CharField(max_length=10000000, null=True),
        ),
    ]
