# -*- coding:utf-8 -*-

from __future__ import absolute_import
from .models import SimpleTask
from django.utils import timezone
from celery import task

@task(bind=True)
def cron_task(self):
    task = SimpleTask(task_name='test')
    task.finish_time = timezone.now()
    task.save()