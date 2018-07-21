# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 21:24:00
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 


import threading
import time


def add(sem,a):
    sem.acquire()
    a += 1
    a -= 1
    print threading.currentThread().name
    print threading.activeCount()
    time.sleep(2)
    sem.release()

def ctrlThread(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':

    sem = threading.Semaphore(3)
    threads = []
    for i in range(10):
        t = threading.Thread(target = add, args =(sem,1))
        threads.append(t)
    ctrlThread(threads)
