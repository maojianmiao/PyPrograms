# -*- coding: utf-8 -*-
# @Date    : 2018-08-07 11:25:13
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

from __future__ import absolute_import
from celery import Celery
app = Celery()
app.config_from_object('config')

if __name__ == '__main__':
    app.start()