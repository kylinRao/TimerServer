# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TSapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=30)),
                ('remindTime', models.CharField(max_length=50)),
                ('remindTitle', models.CharField(max_length=60)),
                ('remindDetail', models.CharField(max_length=30)),
            ],
        ),
    ]