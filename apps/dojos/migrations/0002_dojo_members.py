# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0002_auto_20171008_1136'),
        ('dojos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='members',
            field=models.ManyToManyField(related_name='member_of_dojos', to='ninjas.Ninja'),
        ),
    ]
