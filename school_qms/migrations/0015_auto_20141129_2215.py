# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0014_auto_20141125_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
                ('activity', models.TextField(default='')),
                ('documents', models.ManyToManyField(to='school_qms.Document')),
                ('onwer', models.ForeignKey(to='school_qms.Agent', default='')),
                ('procedure', models.ForeignKey(to='school_qms.Procedure')),
                ('when_distribute', models.ManyToManyField(to='school_qms.Times', default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together=set([('procedure', 'order')]),
        ),
    ]
