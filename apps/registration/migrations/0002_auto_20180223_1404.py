# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
    ]