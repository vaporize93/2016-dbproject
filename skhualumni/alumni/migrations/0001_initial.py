# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=11)),
                ('pw', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('period', models.IntegerField()),
                ('position', models.CharField(max_length=15)),
                ('position_all', models.CharField(max_length=15)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('work', models.CharField(blank=True, max_length=45)),
                ('work_phone', models.CharField(blank=True, max_length=14)),
                ('work_position', models.CharField(blank=True, max_length=45)),
                ('open_login_id', models.BooleanField()),
                ('open_email', models.BooleanField()),
                ('open_picture', models.BooleanField()),
                ('open_work', models.BooleanField()),
                ('open_work_phone', models.BooleanField()),
                ('open_work_position', models.BooleanField()),
            ],
            options={
                'ordering': ('id',),
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'db_table': 'user',
            },
        ),
    ]
