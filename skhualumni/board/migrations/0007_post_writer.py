# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_remove_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
