# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enrollment.models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20160325_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='subject',
            field=models.TextField(verbose_name=enrollment.models.Subject),
        ),
    ]
