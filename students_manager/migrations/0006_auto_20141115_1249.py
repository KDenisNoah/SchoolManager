# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0005_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name_1',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_2',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
