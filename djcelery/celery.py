# -*- coding:utf-8 -*-

from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings')
app = Celery('core')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# CELERYBEAT_SCHEDULE = {
#     'add-every-30-seconds':{
#         'task': 'core.tasks.cron_task',
#         'schedule': timedelta(seconds=30),
#     }
# }

@app.task(bind=True)
def debug_task(self):
    print ('Request: {0!r}'.format(self.request))