# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ninjas', '0002_auto_20171008_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users_using_avatar', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='ninjas.Ninja')),
            ],
        ),
    ]
