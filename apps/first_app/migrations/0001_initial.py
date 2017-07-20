# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Manufacturer', models.CharField(max_length=255)),
                ('Make', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
