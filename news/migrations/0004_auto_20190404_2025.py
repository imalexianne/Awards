# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-04 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_projectmerch'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProjectMerch',
            new_name='CoreProject',
        ),
    ]
