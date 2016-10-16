# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-28 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notizzeile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('name_autor', models.CharField(blank=True, max_length=20, null=True)),
                ('erstelldatum', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]