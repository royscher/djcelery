# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import random
import time

class SimpleTask(models.Model):
    task_name = models.CharField(max_length=64, null=True)
    start_time = models.DateTimeField('task begin time', default=timezone.now)
    finish_time = models.DateTimeField('task end time', blank=True, null=True)

def run_simple_task(task_name):
    task = SimpleTask(task_name=task_name)
    task.finish_time = timezone.now()
    task.save()

