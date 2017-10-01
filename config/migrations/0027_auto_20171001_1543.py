# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 15:43
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0026_auto_20171001_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text_de',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text_es',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_text_zh',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430 '\u041e \u043d\u0430\u0441'"),
        ),
    ]
