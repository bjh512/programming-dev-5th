# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20160717_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='num',
            field=models.IntegerField(),
        ),
    ]
