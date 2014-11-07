# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
    ]
