# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0018_procedure_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.TextField()),
                ('goal', models.TextField()),
                ('indicador', models.TextField()),
                ('method', models.TextField()),
                ('frecuency', models.TextField()),
                ('form', models.ForeignKey(to='school_qms.Document')),
                ('owner', models.ForeignKey(to='school_qms.Agent')),
                ('process', models.ForeignKey(to='school_qms.Process')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='detailedProcess',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('inputs', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('activities', models.TextField()),
                ('output', models.TextField()),
                ('owner', models.ForeignKey(default=1, to='school_qms.Agent')),
                ('process', models.ForeignKey(to='school_qms.Process', related_name='parent_process')),
                ('related_process', models.ForeignKey(to='school_qms.Process', related_name='related_process')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subProcess',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='process',
            name='code',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='customers',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='end_activity',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='instructions',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='legislation',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='owner',
            field=models.ForeignKey(default=1, to='school_qms.Agent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='providers',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='rev',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='scope',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='start_activity',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='process',
            name='subprocess',
            field=models.ManyToManyField(to='school_qms.subProcess'),
            preserve_default=True,
        ),
    ]
