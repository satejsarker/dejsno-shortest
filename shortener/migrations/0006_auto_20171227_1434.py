# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20171223_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
