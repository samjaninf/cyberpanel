# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from websiteFunctions.models import Websites
# Create your models here.

class ContainerLimits(models.Model):
    owner = models.ForeignKey(Websites, on_delete=models.PROTECT)
    cpuPers = models.CharField(max_length=10)
    IO = models.CharField(max_length=10)
    IOPS = models.CharField(max_length=10)
    memory = models.CharField(max_length=10)
    networkSpeed = models.CharField(max_length=10)
    networkHexValue = models.CharField(max_length=10)
    enforce = models.IntegerField(default=0)
