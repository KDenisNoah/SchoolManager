# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_course_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['number']},
        ),
        migrations.AddField(
            model_name='group',
            name='language',
            field=models.TextField(default='D'),
            preserve_default=False,
        ),
    ]
