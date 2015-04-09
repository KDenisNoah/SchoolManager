# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0012_auto_20141125_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='when_distribute',
            field=models.ManyToManyField(to='school_qms.Times', default=''),
        ),
    ]
