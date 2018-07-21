#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Jul 6, 2016

@author: maojianmiao
'''
import sys
sys.path.append(r'D:\Projects\NewsSpider\src')
import spider
import time
from scrapy.selector import Selector
from newsDict import newsDict
reload(sys)
sys.setdefaultencoding( "utf-8" )

class ifeng(spider.spider):
    
    baseUrl = 'http://www.ifeng.com'
    siteName = 'ifeng'
    
    
    def run(self):
        self.crawlTime = time.strftime('%Y-%m-%d %H:%M:%S.000',time.localtime())
        source = self.requestDataFromFile('ifeng.txt')
        dicts = self.parseSource(source)
        if dicts:
            self.storeToDB(dicts)
            for i in dicts:
                print i
                
        self.updatePosition()
        
    def parseSource(self,source):
        pass
    
    def updatePosition(self):
        super.updatePostition(self.crawlTime, self.siteName)

class ifengFinance(spider.spider):
    baseUrl = 'http://finance.ifeng.com/'
    siteName = 'ifeng'
    #source = self.requestDataFrom(self.baseUrl)
    newsType = 5 #财经
    
    def run(self):
        #self.getPageSource(self.baseUrl,'finance.txt')
        self.crawlTime = time.strftime('%Y-%m-%d %H:%M:%S.000',time.localtime())
        
        self.getsource()
        topics = self.parseSource()
        self.storeToDB(topics)
        #for i in topics:
            #print i['title']
        self.updatePostition()
    
    def parseSource(self):
        topics = self.source.xpath('//a')
        
        for i in topics:
            title = i.xpath('./text()').extract_first()
            link = i.xpath('./@href').extract_first()
            
            if (not link) or (not title):
                continue
            
            if not title.strip():
                continue
            
            if len(title.strip())<10 or len(title)>50:
                continue

            if not link.endswith('html'):
                continue
                
            result = self.querySearch('''SELECT ID FROM Topic where Title="{}"'''.format(title.strip()))
            
            print result
            if result:
                print title,' 已经在数据库了'
                continue
            
            topicDict = newsDict()
            topicDict['title'] = title.strip()
            topicDict['link'] = link
            topicDict['publishDate'] = time.strftime('%Y-%m-%d %H:%M:%S.000',time.localtime())
            topicDict['newstypeID'] = self.newsType
            topicDict['siteID'] = 2
            
            yield topicDict
                
    def getsource(self):
        #self.source = self.requestDataFromFile('finance.txt')
        self.source = self.requestDataFrom(self.baseUrl)
        
    def updatePostition(self):
        super(ifengFinance,self).updatePostition(self.crawlTime, self.siteName)

ife = ifengFinance()
ife.run()