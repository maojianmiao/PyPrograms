#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Aug 16, 2016

@author: maojianmiao
'''
import os
import urllib2
import urllib
import glob

#需要查找的包名
patches = []

#PATCH可能存在的LST，可自行添加或删除。
lst = [
]

#下载地址等于baseUrl + lst，注意如果想添加SCA的话得添加架构和语言路径如:x86_64/cs/apps.lst
baseUrl = ""

def downloadFile(filename, baseURL):
    url = baseURL + urllib.quote(filename)#网址编码，去除特殊字符，避免http服务识别网址失败
    try:
        f = urllib2.urlopen(url)
        print('Storing file: {}'.format(filename))
        if not os.path.exists('windows'):
            os.makedirs('windows')
        with open('windows\\' + filename,'wb') as content:
            content.write(f.read())
    except Exception,e:
        print 'Please make sure your URL is right\n', e

def lstFile(path):
    return glob.glob(path + '/*.lst')

#主函数
def main():
    #NOTE:如果LST已经存在,就不会再重新下载了。
    for l in lst:
        if not os.path.exists('windows/' + l):
            downloadFile(l,baseUrl)
    result = open('result.txt','wb')
    for i in patches:
        inlst = ''
        for f in lstFile('windows'):
            with open(f,'rb') as data:
                if i in data.read():
                    inlst += f.strip('windows\\') + ','
        print i,' | ',inlst
        result.write(i+' | '+inlst+'\n')
    result.flush()
    result.close()
    
if __name__ == '__main__':
    main()