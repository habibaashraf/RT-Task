# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=500)),
                ('Phone', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=250)),
                ('Comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
