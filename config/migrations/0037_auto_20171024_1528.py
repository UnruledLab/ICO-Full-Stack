# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0036_auto_20171024_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='investments_eth',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='investments_participants',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='investments_eth_hard',
            field=models.IntegerField(default=0, verbose_name='\u0418\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043e ETH (Hard Cap)'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='investments_eth_soft',
            field=models.IntegerField(default=0, verbose_name='\u0418\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043e ETH (Soft Cap)'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='investments_participants_hard',
            field=models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0432\u0448\u0438\u0445 (Hard Cap)'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='investments_participants_soft',
            field=models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0432\u0448\u0438\u0445 (Soft Cap)'),
        ),
    ]
