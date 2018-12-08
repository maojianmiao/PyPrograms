# -*- coding: utf-8 -*-
# @Date    : 2018-08-07 11:25:33
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

from datetime import timedelta
from kombu import Exchange,Queue

BROKER_URL = 'redis://10.9.198.49:6379'
CELERY_RESULT_BACKEND = 'redis://10.9.198.49:6380'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
CELERY_IMPORTS=("tasks",)
#CELERYD_CONCURRENCY = 4 #并发数，默认为cpu个数
CELERY_QUEUES = (
    Queue("default",Exchange("default"),routing_key="default"), 
    Queue("checkResult",Exchange("checkResult"),routing_key="checkResult"),
    Queue("checkInterface",Exchange("checkInterface"),routing_key="checkInterface") 
   )
    
CELERY_ROUTES = {
    'tasks.transfer':{"queue":"checkResult","routing_key":"checkResult"},
    'tasks.send':{"queue":"checkInterface","routing_key":"checkInterface"},
 } 

ELERYBEAT_SCHEDULE = {
   'ptask': {
       'task': 'tasks.period',
      'schedule': timedelta(seconds=5),
   },
   }