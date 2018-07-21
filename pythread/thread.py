#!c:\Python27\python.exe
#coding:utf-8
'''
Created on Mar 17, 2016

@author: maojianmiao
'''

import threading
import requests
import urllib2
import sys
import time
import download
import logging
import re

class DownloadFile(threading.Thread):
    data = "" #The data which function download get
    path = "" #path where you want to store your file
    url = "" #file url
    def __init__(self,url,path):
        threading.Thread.__init__(self)
        self.url = url
        self.path = path
        
    def run(self):
        #threading.Lock()
        self.req()
        self.storefile()
        time.sleep(2)
    
    def req(self):
        try:
            logging.info("Begin to get data from internet")
            
            #r = urllib2.Request(self.url)
            header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                      'Accept':'text/html;q=0.9,*/*;q=0.8',
                      'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                      'Accept-Encoding':'gzip',
                      'Connection':'close',
                      'Referer':None}
            r = requests.get(self.url,headers = header)
            self.data = r.content
            time.sleep(1)    
        except Exception,e:
            logging.error("Failed to get data from internet: %s",e)
    def storefile(self):
        try:
            logging.info("Storing file...")
            with open(self.path,"wb") as file:
                file.write(self.data)
                #img.write(self.url) #test write
            logging.info("%s is stored",self.path)
            logging.info("%s is completed",self.name)
        except Exception,e:
            logging.error("Failed to Store %s: %s",self.path,e)

def ThreadCtl(threadList,MaxActiveThread):
    for t in threadList:
        if threading.activeCount() < MaxActiveThread:
            t.start()
            logging.info("%s is running",t.getName())
        else:
            logging.warning("Waiting these %s thread complete",threading.activeCount())
            for t in threading.enumerate():
                if t is threading.currentThread():
                    continue
                t.join()             
 ##       
plf = open('PLF.txt','r')
urls = plf.read().split('\n')
plf.close()

def main():
    ####logging setting：同时输出到文件和控制台
    logging.basicConfig(filemode="w",filename="DEBUG.LOG",level=logging.INFO,format="%(asctime)s %(levelname)s: %(message)s",datefmt="%m/%d/%Y %p %I:%M:%S")
    #logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s: %(message)s",datefmt="%m/%d/%Y %p %I:%M:%S")
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)16s %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
    thread = []
    for i in urls:
        t = DownloadFile('http://172.16.46.104/'+i,'plf/'+i)
        thread.append(t)
        logging.info('Add %s to thread list',t.getName())
    #依次执行线程
    ThreadCtl(thread,20)
    logging.info('Over, enjoy yourself')
#########################################
#############--Main--####################
#########################################
main()

