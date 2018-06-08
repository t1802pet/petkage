# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20180605_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', '수컷'), ('f', '암컷'), ('o', '중성')], max_length=1, verbose_name='성별'),
        ),
    ]
