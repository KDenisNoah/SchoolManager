# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_manager', '0003_student_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='text',
            new_name='name',
        ),
    ]
