# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0004_internship_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='aval',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='eligiblity',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='intern_detail',
            field=models.TextField(null=True),
        ),
    ]
