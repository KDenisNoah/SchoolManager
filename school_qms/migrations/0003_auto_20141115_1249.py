# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0002_procedure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='process',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
