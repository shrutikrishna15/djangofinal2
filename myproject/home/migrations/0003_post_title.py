# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180801_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='TITLE', max_length=500),
        ),
    ]
