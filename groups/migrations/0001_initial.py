# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgperson', '0003_auto_20160322_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, default='')),
                ('number', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, default='')),
                ('course', models.ForeignKey(to='groups.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group_Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(to='groups.Group')),
                ('student', models.ForeignKey(to='orgperson.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, default='')),
                ('course', models.ForeignKey(to='groups.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grouping_Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(to='groups.Grouping')),
                ('student', models.ForeignKey(to='orgperson.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grouping',
            name='students',
            field=models.ManyToManyField(through='groups.Grouping_Membership', to='orgperson.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grouping',
            name='year',
            field=models.ForeignKey(to='groups.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(through='groups.Group_Membership', to='orgperson.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='year',
            field=models.ForeignKey(to='groups.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.ForeignKey(to='groups.Year'),
            preserve_default=True,
        ),
    ]
