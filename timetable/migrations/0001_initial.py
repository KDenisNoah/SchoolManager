# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0012_auto_20150410_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hour', models.IntegerField(default='1')),
                ('day', models.IntegerField(default='1')),
                ('subject', models.TextField(max_length=50, default='')),
                ('grouping', models.ForeignKey(to='students_manager.Grouping')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
