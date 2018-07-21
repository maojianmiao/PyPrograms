'''
Created on 2016-5-29

@author: jm
'''
import unittest
import json
import re
import sqlite3
import urllib2
import spider
import glob
from scrapy.selector import Selector

class Test(unittest.TestCase):

    def test_spider_sql_connect(self):
        mys = spider.spider()
        conn = mys.connect()
        conn.close()
    
    @unittest.skip('passed')
    def test_spider_getPageSource(self):
        myspy = spider.spider()
        myspy.getPageSource('http://www.ifeng.com/', 'ifeng.txt')
        
    def test_getPosition(self):
        print spider.getPosition('cnBeta')
    
    def test_storeToDB(self):
        key = ['title', 'comments','link', 'siteID', 'views', 'recommends', 'pointOfIncident', 'pointsOfQuality','guide', 'newstypeID','publishDate']
        data = ['test',6,'/articles/505827.htm',1,2244,1,-3,-5,None,1,'2016-05-30 09:45:31']
        d = [dict(zip(key,data))]
        print d
        myspi = spider.spider()
        myspi.storeToDB(d)
        
if __name__ == "__main__":
    unittest.main()