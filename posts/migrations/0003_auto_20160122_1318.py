# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_dame_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dame_id',
            new_name='game_id',
        ),
    ]
