# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-30 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170430_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='click_history',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='label',
            field=models.TextField(default=''),
        ),
    ]