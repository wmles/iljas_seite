# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Notizzeile(models.Model):
    text = models.CharField(max_length=200)
    name_autor = models.CharField(max_length=20, null=True, blank=True)
    erstelldatum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 15:
            return self.text[:12]+'[...]'
        else: 
            return self.text

