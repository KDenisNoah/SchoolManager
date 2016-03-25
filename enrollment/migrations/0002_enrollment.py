# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20160325_1019'),
        ('orgperson', '0003_auto_20160322_2039'),
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('course', models.ForeignKey(to='groups.Course')),
                ('student', models.ForeignKey(to='orgperson.Student')),
                ('subjects', models.ManyToManyField(to='enrollment.Subject')),
                ('year', models.ForeignKey(to='groups.Year')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
