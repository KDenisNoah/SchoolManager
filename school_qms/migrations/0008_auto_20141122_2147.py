# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0007_auto_20141122_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='descritption',
            new_name='description',
        ),
    ]
