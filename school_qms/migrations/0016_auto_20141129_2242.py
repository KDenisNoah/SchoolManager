# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0015_auto_20141129_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='onwer',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='procedure',
            old_name='onwer',
            new_name='owner',
        ),
    ]
