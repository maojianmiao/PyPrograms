# -*- coding: utf-8 -*-
# @Date    : 2018-08-06 11:00:12
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$
import os
import psutil
def killProcessByName(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        currentName = p.name()
        if currentName == name or currentName == '{}.exe'.format(name):
            try:
                p.terminate()
            except Exception,e:
                pass

if __name__ == '__main__':
    killProcessByName('chromedriver')
    killProcessByName('phantomjs')