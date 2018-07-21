#!c:\Python27\python.exe
#coding:utf-8
'''
Created on Mar 17, 2016

@author: maojianmiao
'''

import threading
import glob
import os
import re
import logging
'''
    存放一些自己日常工作提取出来的实用、通用、常用的函数
'''
#判断文件夹是否为空
def isEmptyDir(dirpath):
    if not dirpath.endswith('\\'):
        dirpath = dirpath + '\\'
            
    dirpath = dirpath.decode() + '*'
        #print dirpath
        #print glob.glob(dirpath)
    if glob.glob(dirpath):
        return False
    else:
        return True
    
#删除空文件夹
def delEmptyDirs(dirpath):
    if not dirpath.endswith('\\'):
        dirpath = dirpath + '\\'    
    items = glob.glob(dirpath.decode() + '*')
    for item in items:
        if os.path.isdir(item):
            if isEmptyDir(item):
                os.rmdir(item)
                print 'remove %s from your PC' % item
            else:
                delEmptyDirs(item)
        else:
            continue
        #wukong.delEmptyDirs(dirpath)
        
#从配置文件夹中获取一个变量字典
#配置文件夹格式：
#var1=1
#var2=2        
def getDict(text):
    List = text.split()
    d = dict()
    for i in List:
        d[i.split('=')[0]] = i.split('=')[1]
    return d

def run(func,*args):
    try:
        func(*args)
        logging.info('passed')
    except Exception,e:
        logging.error('Failed because: %s', e)
        
def hw(a,b):
    print(a)
    print(b)

logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s: %(message)s",datefmt="%m/%d/%Y %p %I:%M:%S")
run(hw,1,2)