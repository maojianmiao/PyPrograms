#!c:\Python27\python.exe
#coding:utf-8
'''
Created on Mar 17, 2016

@author: maojianmiao
'''

import threading
import time
import urllib2
import os
import sys

class Tree:
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        print self.name
    @staticmethod
    def grow():
        pass
    
t =Tree('aa')

print t.name
