#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on May 25, 2016

@author: maojianmiao
'''

import sqlite3

conn = sqlite3.connect(r'..\Notes\news.db')
cur = conn.cursor()
cur.execute("select *from Topic")

for i in cur.fetchall():
    print i
    '''
cur.execute("select * from sqlite_master where type='table'")
for i in cur.fetchall():
    print i
'''
conn.commit()
conn.close()