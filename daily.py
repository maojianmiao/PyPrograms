#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Mar 25, 2016

@author: maojianmiao
'''
import hashlib
import time
import datetime
import sqlite3
import os
import math
import re

def getPosition(siteName):
    conn = sqlite3.connect(r'C:\Users\lauvey\workspace\NewSpider\src\Notes\positon.db')
    cur = conn.cursor()
    query =  "SELECT lasttime FROM crawlTime WHERE siteName='{}'".format(siteName)
    lasttime = cur.execute(query).fetchone()[0]
    conn.close()
    return str(lasttime)[0:-4]


#python读取超大文件的方法。open文件会返回一个file对象，而file对象是一个迭代器
#
def readBigData(filename):
	with open(filename) as f:
		for i in f:
			yield i

def testYield():
    for i in xrange(2):
        yield i 

def prime(n):
    prime = [2,]
    if n == 2:
        return prime

    for num in xrange(3,n+1):
        isprime = True
        for p in prime:
            if p>math.sqrt(num):
                break
            if num % p == 0:
                isprime = False
                break
        
        if isprime:
            prime.append(num)
    return prime

def twoNum(nums,target):
    for i in xrange(len(nums)-1):
        for j in xrange(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

import xlrd
def readexcel(filename):
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(0)

    print sh.cell(4,0).value
    print sh.cell(4,0).ctype

    local = xlrd.xldate_as_tuple(sh.cell_value(4,0),book.datemode)
    print local
    print datetime.date(*local[:3]).strftime('%Y-%m-%d')

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        if n == 2:
            return '11'
        last = self.countAndSay(n - 1)
        
        result = ''
        count = 1
        for i in range(len(last) - 1):
            if last[i] == last[i + 1]:
                count += 1
                continue
            
            else:
                result += str(count) + str(last[i])
                print result
                count = 1
                continue
        
        if len(last)>=2 and last[-1] != last[-2]:
            result += '1' + str(last[-1])
        
        return result


#s = Solution()
#print s.countAndSay(2)
#print s.countAndSay(1)
#print s.countAndSay(4)

if __name__ == '__main__':
    f = open('test.txt')
    s = f.read()
    print '^^^^^^^^^^^^^^^^^^^^^^'
    f.seek(0)
    print f.read()