# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_auto_20160719_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='monster',
            field=models.ManyToManyField(related_name='monster', to='pokemon.Pokemon'),
        ),
    ]