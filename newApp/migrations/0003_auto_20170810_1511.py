# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0002_auto_20170810_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
