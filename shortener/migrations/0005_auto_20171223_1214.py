# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20171221_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
