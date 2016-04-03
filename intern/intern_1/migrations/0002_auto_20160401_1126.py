# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='interncategory',
        ),
        migrations.AddField(
            model_name='internship',
            name='interncategory',
            field=models.ForeignKey(to='intern_1.InternCategory', null=True),
        ),
    ]
