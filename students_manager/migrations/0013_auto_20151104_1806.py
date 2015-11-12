# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0012_auto_20150410_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, to='students_manager.Group', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='groupings',
            field=models.ManyToManyField(to='students_manager.Grouping', blank=True, null=True),
        ),
    ]
