# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0002_auto_20160401_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='image',
            field=models.ImageField(null=True, upload_to=b'ritu'),
        ),
    ]
