# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20180619_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='is_final',
            field=models.BooleanField(default=False),
        ),
    ]