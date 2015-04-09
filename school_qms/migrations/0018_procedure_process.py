# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0017_auto_20141129_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='process',
            field=models.ManyToManyField(default='', to='school_qms.Process'),
            preserve_default=True,
        ),
    ]
