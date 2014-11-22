# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0008_auto_20141122_2147'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='revision',
            unique_together=set([('document', 'number')]),
        ),
    ]
