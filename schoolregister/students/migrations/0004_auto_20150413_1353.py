# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0003_studentnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentnote',
            name='created_by',
            field=models.ForeignKey(related_name='created_notes', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentnote',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 13, 53, 38, 382596, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
