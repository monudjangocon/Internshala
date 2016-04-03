# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern_1', '0005_auto_20160401_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipFill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('starting_date', models.DateField()),
                ('expected_stipend', models.IntegerField()),
                ('months_commit', models.CharField(max_length=10)),
                ('assessment', models.TextField()),
                ('internshhip', models.ForeignKey(to='intern_1.Internship')),
            ],
        ),
    ]
