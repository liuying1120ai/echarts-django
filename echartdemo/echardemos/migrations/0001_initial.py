# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineCharts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xtime', models.DateTimeField(verbose_name=b'linetime')),
                ('value', models.IntegerField(verbose_name=b'linevalue')),
            ],
            options={
                'db_table': 'linecharts',
            },
        ),
    ]
