# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0003_internship_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='posted_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
