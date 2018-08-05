# -*- coding: utf-8 -*-
# @Date    : 2018-08-05 13:36:57
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 

import os 
from multiprocessing import Process
import multiprocessing
import time

def add(a,b):
    print('{} + {} = {}'.format(a, b, a+b))
    time.sleep(2)
    print('run child process: {}'.format(os.getpid()))
    return a + b


def runFunc(func, *args):
    print 'Parent process %s.' % os.getpid()
    processes = list()
    for i in range(5):
        p = Process(target=func, args=args)
        print 'Process will start.'
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    print 'Process end.'

def processPool(func,*args):
    pool = multiprocessing.Pool(processes = 4)
    result = []
    for i in range(6):
        result.append(pool.apply_async(func,args))
    pool.close()
    pool.join()
    for i in result:
        print i.get()

def applyProcessPool(func,*args):
    pool = multiprocessing.Pool(processes = 1)
    result = []
    for i in range(6):
        result.append(pool.apply(func,args))
    pool.close()
    pool.join()

#linux fork
if __name__ == "__main__":
    #runFunc(add,1,2)
    processPool(add,1,2)
    #applyProcessPool(add,1,2)