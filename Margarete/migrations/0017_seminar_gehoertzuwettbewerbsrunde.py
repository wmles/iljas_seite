# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Margarete', '0016_sonstigeveranstaltung_teilnahmearten'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='gehoertzuwettbewerbsrunde',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Margarete.Wettbewerbsrunde'),
        ),
    ]
