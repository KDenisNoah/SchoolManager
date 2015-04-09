# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_qms', '0011_procedure_onwer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('month', models.CharField(choices=[('00', 'When Needed'), ('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'Dececember')], max_length=2, default='0')),
                ('week', models.CharField(choices=[('0', 'Wheen Needed'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], max_length=1, default='0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='when_distribute',
            field=models.ManyToManyField(to='school_qms.Times', default=1),
            preserve_default=True,
        ),
    ]
