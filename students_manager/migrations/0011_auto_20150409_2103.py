# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0010_auto_20141119_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=10, default='')),
                ('year', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=10, default='')),
                ('course', models.ForeignKey(to='students_manager.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.ForeignKey(to='students_manager.Course', default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='students_manager.Group', default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='groupings',
            field=models.ManyToManyField(to='students_manager.Grouping'),
            preserve_default=True,
        ),
    ]
