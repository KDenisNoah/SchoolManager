# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20160325_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(max_length=2, choices=[('1', '8.30-9.25'), ('2', '9.25-10.20'), ('3', '10.20-11.15'), ('FT', '11-15-11.45'), ('4', '11.45-12.40'), ('5', '12.40-13.35'), ('6', '13.35-14.30')]),
        ),
    ]
