# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0002_auto_20141107_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='text',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
