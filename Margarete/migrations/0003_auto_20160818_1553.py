# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Margarete', '0002_auto_20160816_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='artteilnahme',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fachbereich',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='konkretewettbewerbsrunde',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seminar',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teilnahmekonzept',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veranstaltung',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wettbewerb',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wettbewerbsrunde',
            name='urlbezeichnung',
            field=models.SlugField(default='l', max_length=60),
            preserve_default=False,
        ),
    ]
