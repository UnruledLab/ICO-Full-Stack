# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20170922_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammate',
            name='category',
        ),
        migrations.DeleteModel(
            name='TeammateCategory',
        ),
    ]
