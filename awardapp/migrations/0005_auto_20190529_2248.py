# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0004_remove_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]