# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('latest_hour', models.IntegerField(default=0)),
                ('total_hour', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_activity', models.ForeignKey(default=0, to='tentacle.Activity')),
            ],
        ),
    ]
