# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-21 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20171221_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
