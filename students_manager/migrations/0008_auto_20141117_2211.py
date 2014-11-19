# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0007_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name_1',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name_2',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(default='', max_length=50),
        ),
    ]
