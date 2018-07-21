#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Jul 6, 2016

@author: maojianmiao
'''

class newsDict(dict):
    def __init__(self):
        self['title'] = ''
        self['link'] = ''
        #print topic.xpath('.//*[@class="title"]/a/text()').extract_first()
        self['publishDate'] = ''
        self['views'] = 1
        self['comments'] = 1
        self['recommends'] = 1
        self['judges'] = 0
        self['pointOfIncident'] = 0
        self['pointsOfQuality'] = 0    
        self['siteID'] = 0
        self['guide'] = None
        self['newstypeID'] = 1
    