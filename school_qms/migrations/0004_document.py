# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0003_auto_20141115_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default='')),
                ('descritption', models.TextField(default='')),
                ('code', models.TextField(default='')),
                ('record', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('disabled_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('creation_date', models.DateField(default=datetime.datetime.now)),
                ('aprobation_date', models.DateField(default=datetime.datetime.now)),
                ('document_file', models.FileField(upload_to='documents', blank=True)),
                ('document_url', models.URLField(blank=True)),
                ('procedure', models.ForeignKey(to='school_qms.Procedure')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
