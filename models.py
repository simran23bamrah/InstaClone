# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TestTable(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

