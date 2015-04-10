# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0011_auto_20150409_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='groupings',
            field=models.ManyToManyField(null=True, to='students_manager.Grouping'),
        ),
    ]
