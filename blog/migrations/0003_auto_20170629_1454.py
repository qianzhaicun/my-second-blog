# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_commit',
            new_name='approved_comment',
        ),
    ]
