# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-29 10:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wholesale', '0020_newrelease_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('info_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='order_id')),
                ('business_name', models.CharField(max_length=100, null=True, verbose_name='business_name')),
                ('address', models.CharField(max_length=10000000, null=True, verbose_name='address')),
                ('town', models.CharField(max_length=100, null=True, verbose_name='town')),
                ('post_code', models.CharField(max_length=10000000, null=True, verbose_name='post_code')),
                ('phone', models.CharField(max_length=10000000, null=True, verbose_name='phone')),
                ('fax', models.CharField(max_length=10000000, null=True, verbose_name='fax')),
                ('contact_name', models.CharField(max_length=10000000, null=True, verbose_name='contact_name')),
                ('delivery', models.CharField(max_length=10000000, null=True, verbose_name='delivery')),
                ('delivery_instructions', models.CharField(max_length=10000000, null=True, verbose_name='delivery_instructions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]