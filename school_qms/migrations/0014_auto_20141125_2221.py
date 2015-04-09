# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0013_auto_20141125_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='onwer',
            field=models.ForeignKey(related_name='agents', default=1, to='school_qms.Agent'),
        ),
        migrations.AlterField(
            model_name='document',
            name='recipients',
            field=models.ManyToManyField(default='', to='school_qms.Agent', related_name='recipients'),
        ),
    ]
