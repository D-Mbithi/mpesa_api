# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_c2brequest_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='c2brequest',
            name='transaction_id',
            field=models.CharField(default='', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]