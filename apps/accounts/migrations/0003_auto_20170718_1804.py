# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170715_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='email',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='user', max_length=60),
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
