# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-02 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
