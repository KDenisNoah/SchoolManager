# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgperson', '0002_staff_stype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='picture',
        ),
        migrations.AddField(
            model_name='staff',
            name='picture',
            field=models.ImageField(blank=True, upload_to='staff/', null=True, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, upload_to='students/', null=True, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(blank=True, upload_to='teachers/', null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staff',
            name='stype',
            field=models.CharField(choices=[('O', 'Office'), ('G', 'Gatekeeper'), ('C', 'Computer Technician'), ('M', 'Maintenance Technician')], max_length=1),
        ),
    ]
