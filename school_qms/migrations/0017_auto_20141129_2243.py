# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0016_auto_20141129_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='onwer',
            new_name='owner',
        ),
    ]
