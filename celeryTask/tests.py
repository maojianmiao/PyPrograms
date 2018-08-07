# -*- coding: utf-8 -*-
# @Date    : 2018-08-07 20:02:52
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

from tasks import *

if __name__ == '__main__':
    #send(123123)
    for i in range(10):
        b = send.delay(i)
        #a = transfer.delay(i,1)
        #print a.status,b.status