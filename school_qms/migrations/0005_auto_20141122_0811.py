# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0004_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='disabled_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(upload_to='documents', null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_url',
            field=models.URLField(null=True),
        ),
    ]
