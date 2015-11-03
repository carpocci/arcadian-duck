# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview',
        ),
    ]
