# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='stype',
            field=models.CharField(default='G', max_length=1, choices=[('O', 'OFfice'), ('G', 'Gatekeeper'), ('C', 'Computer Technician'), ('M', 'Maintenance Technician')]),
            preserve_default=False,
        ),
    ]
