# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tentacle', '0002_auto_20150909_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.ForeignKey(to='tentacle.Activity')),
            ],
        ),
    ]
