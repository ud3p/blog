# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='step_2',
            field=models.TextField(default='2. ', verbose_name='\u0428\u0430\u0433_2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='step_3',
            field=models.TextField(default='3. ', verbose_name='\u0428\u0430\u0433_3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='step_4',
            field=models.TextField(default='4. ', verbose_name='\u0428\u0430\u0433_4'),
            preserve_default=True,
        ),
    ]
