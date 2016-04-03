# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0006_internshipfill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipfill',
            name='internshhip',
            field=models.ForeignKey(to='intern_1.Internship', null=True),
        ),
    ]
