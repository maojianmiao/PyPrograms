# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 22:49:59
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 

import time
from functools import wraps

def countTime(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        starttime = time.time()
        f(*args,**kwargs)
        endtime = time.time()

        p = (endtime - starttime) * 1000
        print('execute time: %s' % p)

    return wrapper
@countTime
def sum(a,b):
    print a + b
    time.sleep(1)

if __name__ == '__main__':
    print sum.__name__