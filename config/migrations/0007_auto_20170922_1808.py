# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20170922_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='team_block_title',
            field=models.CharField(default='Team', max_length=128, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='team_block_title_en',
            field=models.CharField(default='Team', max_length=128, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='team_block_title_ru',
            field=models.CharField(default='Team', max_length=128, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='team_block_title_zh',
            field=models.CharField(default='Team', max_length=128, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
    ]
