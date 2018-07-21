#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on May 25, 2016

@author: maojianmiao
'''
## manage News.DB
import sqlite3

conn  = sqlite3.connect('news.db')
cur = conn.cursor()
"""
cur.execute('''create table Topic(
    ID             INTEGER PRIMARY KEY AUTOINCREMENT,
    Title         VARCHAR(100),
    Comments     INT  UNSIGNED,
    Link         VARCHAR(100),
    SiteID         SMALLINT UNSIGNED,
    Views         INT  UNSIGNED,
    Recommends  INT  UNSIGNED,
    StoryPoints         INT,
    QulaityPoints     INT,
    Guide             TEXT,
    NewsTypeID         TINYINT
)''')

cur.execute('''CREATE TABLE NewsType(
    NewsTypeID     INTEGER PRIMARY KEY AUTOINCREMENT,
    NewsTypeName VARCHAR(20),
    Description        TINYTEXT
)''')

cur.execute('''CREATE TABLE Sites(
    SiteID    INTEGER PRIMARY KEY AUTOINCREMENT,
    SiteName    VARCHAR(12),
    Link    VARCHAR(30)    
)''')
"""
#cur.execute("INSERT INTO Topic values(null, 'tech',23,'http://aa.com',3,4,1,2,3,'asd',1)")
cur .execute("ALTER TABLE Topic ADD publicDate text")
conn.commit()
conn.close()

print('Over')