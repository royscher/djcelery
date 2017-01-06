# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from tasks import cron_task

# Create your views here.

class MyTask(View):
    def get(self, request, *args, **kwargs):
        cron_task.delay()
        return HttpResponse('django and celery.')
