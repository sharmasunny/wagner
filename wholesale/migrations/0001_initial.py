# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-22 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ColourClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Colour classes',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=300)),
                ('town', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=6)),
                ('phone_no', models.CharField(max_length=12)),
                ('fax_no', models.CharField(max_length=12)),
                ('contact_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('delivery_instructions', models.TextField(max_length=300)),
                ('prefer_two_year_old', models.BooleanField(default=False)),
                ('deposit_by_april', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_no', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=6)),
                ('colour_class', models.CharField(max_length=3)),
                ('protected_variety', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Product categories',
            },
        ),
    ]
