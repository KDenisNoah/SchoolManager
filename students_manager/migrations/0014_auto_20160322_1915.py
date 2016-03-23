# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0013_auto_20151104_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groupings',
        ),
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='educacode',
            field=models.TextField(max_length=10, unique=True, default='update'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(null=True, max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.TextField(choices=[('H', 'Female'), ('M', 'Male')], default='M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.TextField(null=True, max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='uniquename',
            field=models.TextField(max_length=10, unique=True, default='update'),
            preserve_default=False,
        ),
    ]
