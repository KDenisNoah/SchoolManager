# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField(default='', max_length=50)),
                ('last_name_1', models.TextField(default='', max_length=50)),
                ('last_name_2', models.TextField(default='', max_length=50)),
                ('educacode', models.TextField(max_length=10, unique=True)),
                ('uniquename', models.TextField(max_length=10, unique=True)),
                ('gender', models.CharField(max_length=1, choices=[('H', 'Female'), ('M', 'Male')])),
                ('email', models.EmailField(blank=True, max_length=75, null=True)),
                ('picture', models.ImageField(default=None, blank=True, upload_to='/', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='teachers.Person', serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('teachers.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='teachers.Person', serialize=False, parent_link=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('nationality', models.TextField(blank=True, max_length=20, null=True)),
            ],
            options={
            },
            bases=('teachers.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='teachers.Person', serialize=False, parent_link=True)),
            ],
            options={
            },
            bases=('teachers.person',),
        ),
    ]
