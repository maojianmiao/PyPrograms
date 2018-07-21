#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Apr 18, 2016

@author: maojianmiao
'''
import sys
sys.path.append(r'D:\Projects\NewsSpider\src')
import spider
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class cnbeta(spider.spider):
    
    baseUrl = 'http://www.cnbeta.com/'
    siteName = 'cnBeta' 
    
    def run(self):
        topics = self.requestDataFrom(self.baseUrl)
        self.crawlTime = time.strftime('%Y-%m-%d %H:%M:%S.000',time.localtime())
        dicts = self.parseSource(topics)
        if dicts:
            self.storeToDB(dicts)
        
        self.updatePostition()
            
    def parseSource(self,source):
            for topic in source.xpath('//div[@class="item"]'):
                dictTopic = dict()
                publishDate = topic.xpath('.//*[@class="title"]/div//span/em/text()').extract()[0]
                pos = spider.getPosition('cnBeta')
                
                if not spider.compareTime(publishDate, pos):
                    continue
            
                dictTopic['title'] = topic.xpath('.//*[@class="title"]/a/text()').extract_first()
                if not dictTopic['title']:
                    dictTopic['title'] = topic.xpath('.//*[@class="title"]/a/span/text()').extract_first()
                    
                dictTopic['link'] = topic.xpath('.//*[@class="title"]/a/@href').extract_first()
                #print topic.xpath('.//*[@class="title"]/a/text()').extract_first()
                dictTopic['publishDate'] = publishDate
                dictTopic['views'] = int(topic.xpath('.//*[@class="title"]/div//span/em/text()').extract()[1])
                dictTopic['comments'] = int(topic.xpath('.//ul/li[2]/em/text()').extract_first())
                dictTopic['recommends'] = int(topic.xpath('.//ul/li[3]/em/text()').extract_first())
                dictTopic['judges'] = int(topic.xpath('.//ul/li[4]/em/text()').extract_first())
                dictTopic['pointOfIncident'] = int(topic.xpath('.//ul/li[5]/em/text()').extract_first())
                dictTopic['pointsOfQuality'] = int(topic.xpath('.//ul/li[6]/em/text()').extract_first())
                
                dictTopic['siteID'] = 1
                dictTopic['guide'] = None
                dictTopic['newstypeID'] = 1
                
                yield dictTopic
        
    def store(self):
        super(cnbeta,self).store(list(self.run()),'cnbeat.json')
    
    def updatePostition(self):
        super(cnbeta,self).updatePostition(self.crawlTime, self.siteName)
     
flow = cnbeta()
flow.run()

