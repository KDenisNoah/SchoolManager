# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20160324_1855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('name', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='grouping',
            unique_together=set([('name', 'year')]),
        ),
    ]
