# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20160325_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField(default='', max_length=50)),
                ('shortname', models.TextField(default='', max_length=50)),
                ('abv', models.TextField(default='', max_length=5)),
                ('stype', models.CharField(choices=[('C', 'Common'), ('O', 'Optional'), ('M', 'Moral'), ('P', 'Propedeutic')], max_length=1)),
                ('course', models.ForeignKey(to='groups.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
