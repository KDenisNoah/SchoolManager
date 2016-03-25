# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgperson', '0003_auto_20160322_2039'),
        ('timetable', '0002_auto_20150414_1006'),
        ('groups','0004_auto_20160325_1019')
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(to='orgperson.Teacher', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.IntegerField(max_length=2, choices=[('1', '8.30-9.25'), ('2', '9.25-10.20'), ('3', '10.20-11.15'), ('FT', '11-15-11.45'), ('4', '11.45-12.40'), ('5', '12.40-13.35'), ('6', '13.35-14.30')]),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='grouping',
            field=models.ForeignKey(to='groups.Grouping'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='hour',
            field=models.CharField(max_length=2, choices=[('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday')]),
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set([('day', 'hour', 'teacher'), ('day', 'hour', 'grouping')]),
        ),
    ]
