#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Apr 18, 2016

@author: maojianmiao
'''
import urllib2
import urllib
import logging
import xml.etree.ElementTree as ET
from scrapy.selector import Selector
import json
import sqlite3
import time

class spider(object):
    baseUrl = '' # http://www.example.com/
    siteName = ''
    dbDir = 'D:\\Projects\\NewsSpider\\src\\Notes\\'
    
    def requestDataFrom(self,url):
        url = self.formatUrl(url)
        print url
        try:
            data = urllib2.urlopen(url,timeout=120).read()
            logging.info('Retrived the data from %s successfully', url)
            return Selector(text=data)
        except Exception,e:
            logging.error('Failed to get data from %s', url)
            
    def requestDataFromFile(self,filename):
        try:
            f = open(filename,'rb')
            data = f.read()
            f.close()
            return Selector(text=data)
        except Exception,e:
            logging.error('Failed to get data from file: %s', filename)
            
    def formatUrl(self,url):
        if url.startswith('http'):
            return url
        elif url.startswith('www'):
            return 'http' + url
        else:
            url = self.baseUrl + url
            return url.replace('//','/')
        
    def getPageSource(self,url,file):
        data = urllib2.urlopen(url,timeout=120).read()
        f = open(file,'w')
        f.write(data)
        f.close()
        
    def store(self,myDict,jsonFile):
        f = open(jsonFile,'w')
        json.dump(myDict,f,indent=0)
        f.close()
    
    def connect(self):
        return sqlite3.connect(self.dbDir + 'news.db')
    
    def storeToDB(self,dictSeq):
        ''''
        dicts = self.run()
        if not dicts:
            return
        '''
        conn = self.connect()
        cur = conn.cursor()
        
        for d in dictSeq:
            print d
            query = '''INSERT INTO Topic values(null, "{title}",{comments},"{link}",{siteID},{views},{recommends},{pointOfIncident},{pointsOfQuality},"{guide}",{newstypeID},"{publishDate}")'''.format(**d)
            print query
            cur.execute(query)
            conn.commit()
        conn.close()
    
    def updatePostition(self,time,siteName):
        conn = sqlite3.connect(spider.dbDir + 'news.db')
        cur = conn.cursor()
        query =  "UPDATE crawlTime SET lasttime='{}' WHERE siteName='{}'".format(time,siteName)
        cur.execute(query)
        conn.commit()
        conn.close()

    def querySearch(self,query):
        conn = sqlite3.connect(spider.dbDir + 'news.db')
        cur = conn.cursor()
        result = cur.execute(query).fetchall()
        conn.close()
        return result
 
 #对比时间       
def compareTime(a,position):
    return time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S')) > time.mktime(time.strptime(position, '%Y-%m-%d %H:%M:%S.000'))

#获取上一次爬取数据的时间
def getPosition(siteName):
    conn = sqlite3.connect(spider.dbDir + 'news.db')
    cur = conn.cursor()
    query =  "SELECT lasttime FROM crawlTime WHERE siteName='{}'".format(siteName)
    lasttime = cur.execute(query).fetchone()[0]
    conn.close()
    return str(lasttime)

#更新爬取数据时间
def updatePostition(time,siteName):
    conn = sqlite3.connect(spider.dbDir + 'news.db')
    cur = conn.cursor()
    query =  "UPDATE crawlTime SET lasttime='{}' WHERE siteName='{}'".format(time,siteName)
    cur.execute(query)
    conn.commit()
    conn.close()
