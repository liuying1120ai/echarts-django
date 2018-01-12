# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('echardemos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linecharts',
            name='xtime',
            field=models.TimeField(verbose_name=b'linetime'),
        ),
    ]
