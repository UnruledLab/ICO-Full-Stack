# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0430')),
                ('email', models.EmailField(max_length=254, verbose_name='Email \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u0430')),
                ('subscribed_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430 \u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438 \u043d\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
    ]
