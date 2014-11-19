# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0006_auto_20141115_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(upload_to='/ikasleak/', default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
