# -*- coding: utf-8 -*-
# @Date    : 2018-08-07 10:27:11
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$
from celery import Celery
from initCelery import app
import time
#app = Celery('tasks',broker='redis://10.9.198.49:6379')
#celery -A tasks worker --loglevel=info
#celery -A tasks worker -n worker.%h -Q checkResult --loglevel=info 


@app.task
def transfer(a,b):
    a -= 1
    b += 1
    print('a: {}, b:{}'.format(a,b))
    return a
@app.task
def send(text):
    print "send task: {}".format(text)
    time.sleep(3)
    print "send task done: {}".format(text)
    return text

@app.task
def period():
    print 'period task done'