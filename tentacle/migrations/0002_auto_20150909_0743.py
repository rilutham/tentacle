# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_tentacle_from_fixture(apps, schema_editor):
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "loaddata", "activity"])

class Migration(migrations.Migration):

    dependencies = [
        ('tentacle', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_tentacle_from_fixture),
    ]
