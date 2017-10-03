# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0022_auto_20170929_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(default='40%', max_length=5, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440 \u0441\u043a\u0438\u0434\u043a\u0438')),
                ('discount_text', models.CharField(default='In the first 7 days', max_length=64, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
                ('discount_text_en', models.CharField(default='In the first 7 days', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
                ('discount_text_ru', models.CharField(default='In the first 7 days', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
                ('discount_text_es', models.CharField(default='In the first 7 days', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
                ('discount_text_de', models.CharField(default='In the first 7 days', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
                ('discount_text_zh', models.CharField(default='In the first 7 days', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a \u0441\u043a\u0438\u0434\u043a\u0435')),
            ],
            options={
                'verbose_name': '\u0421\u043a\u0438\u0434\u043a\u0430',
                'verbose_name_plural': '\u0421\u043a\u0438\u0434\u043a\u0438',
            },
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title',
            field=models.CharField(default='Advisors', max_length=64, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title_de',
            field=models.CharField(default='Advisors', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title_en',
            field=models.CharField(default='Advisors', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title_es',
            field=models.CharField(default='Advisors', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title_ru',
            field=models.CharField(default='Advisors', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='advisor_block_title_zh',
            field=models.CharField(default='Advisors', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Advisors'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title',
            field=models.CharField(default='FAQ', max_length=64, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title_de',
            field=models.CharField(default='FAQ', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title_en',
            field=models.CharField(default='FAQ', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title_es',
            field=models.CharField(default='FAQ', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title_ru',
            field=models.CharField(default='FAQ', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='faq_block_title_zh',
            field=models.CharField(default='FAQ', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'FAQ'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_start_link',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0432 \u043a\u043d\u043e\u043f\u043a\u0435 "Start Pre-ICO"'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text_de',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text_en',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text_es',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text_ru',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_block_timer_text_zh',
            field=models.CharField(default='Pre-ICO tokens golfcoin starts through', max_length=64, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u0430\u0439\u043c\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_email',
            field=models.EmailField(default='support@golfcoin.club', max_length=64, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title',
            field=models.CharField(default='Our partners', max_length=64, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title_de',
            field=models.CharField(default='Our partners', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title_en',
            field=models.CharField(default='Our partners', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title_es',
            field=models.CharField(default='Our partners', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title_ru',
            field=models.CharField(default='Our partners', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='partners_block_title_zh',
            field=models.CharField(default='Our partners', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Our partners'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text1_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 1 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text2_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 2 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text3_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 3 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text4_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 4 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text5_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 5 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6_de',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6_en',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6_es',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6_ru',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_text6_zh',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u041f\u043b\u0430\u043d 6 (\u0442\u0435\u043a\u0441\u0442)'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title',
            field=models.CharField(default='Roadmap', max_length=64, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title_de',
            field=models.CharField(default='Roadmap', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title_en',
            field=models.CharField(default='Roadmap', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title_es',
            field=models.CharField(default='Roadmap', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title_ru',
            field=models.CharField(default='Roadmap', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='project_plan_title_zh',
            field=models.CharField(default='Roadmap', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 'Roadmap'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='social_fb',
            field=models.CharField(blank=True, help_text='https://facebook.com/golfco', max_length=64, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Facebook'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='social_in',
            field=models.CharField(blank=True, help_text='https://linkedin.com/golfco', max_length=64, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Linkedin'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='social_insta',
            field=models.CharField(blank=True, help_text='https://instagram.com/golfco', max_length=64, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Instagram'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='social_telegram',
            field=models.CharField(blank=True, help_text='https://t.co/golfco', max_length=64, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Telegram'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='social_twi',
            field=models.CharField(blank=True, help_text='https://twitter.com/golfco', max_length=64, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Twitter'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title',
            field=models.CharField(default='Team', max_length=64, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title_de',
            field=models.CharField(default='Team', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title_en',
            field=models.CharField(default='Team', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title_es',
            field=models.CharField(default='Team', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title_ru',
            field=models.CharField(default='Team', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='team_block_title_zh',
            field=models.CharField(default='Team', max_length=64, null=True, verbose_name="\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0431\u043b\u043e\u043a\u0430 'Team'"),
        ),
        migrations.AddField(
            model_name='discount',
            name='config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='config.SiteConfiguration', verbose_name='\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430'),
        ),
    ]