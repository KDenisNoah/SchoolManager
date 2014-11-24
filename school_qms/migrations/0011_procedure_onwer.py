# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0010_auto_20141124_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='onwer',
            field=models.ForeignKey(default=1, to='school_qms.Agent'),
            preserve_default=True,
        ),
    ]
