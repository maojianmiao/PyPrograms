# -*- coding: utf-8 -*-
# @Date    : 2018-11-27 11:30:56
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

import os

import MySQLdb
import logging
import time

class mysql(object):
    def __init__(self,host, user, passwd, db, port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port

    def getConn(self):
        return self.conn
        
    def start(self):
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=int(self.port),charset="utf8",use_unicode="True")
        except Exception,e:
            logging.error("Cannot connect to SQL host:%s db: %s",self.host,self.db)
            print e
            return False
    
    def query(self,sql_cmd):
        cursor = self.conn.cursor()
        rows = cursor.execute(sql_cmd)
        
        if rows > 0:
            rows = cursor.fetchall()
            cursor.close()
            return rows
        else:
            logging.error("Didn't find any record in the table.")
            return []

    def execute(self,sql_cmd):
        cursor = self.conn.cursor()
        rows = cursor.execute(sql_cmd)
        self.conn.commit()
        if rows > 0:
            cursor.close()
            return True
        else:
            logging.error("Failed to exec sql, please check!")
            return False

    def queryDicts(self,query):
        cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        rows = cur.execute(query)

        if rows > 0:
            rows = cur.fetchall()
            cur.close()
            return rows
        else:
            logging.error("Didn't find any record in the table.")
            return []

    def queryDict(self,query):
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        rows = cur.execute(query)

        if row > 0:
            rows = cur.fetchall()
            cur.close()
            return rows[0]
        else:
            logging.error("Didn't find any record in the table.")
            return {}

    def close(self):
        self.conn.close()
        
if __name__ == "__main__":
    dbinfo = ('1.1.1.1','1','1','1',3306)
    db = mysql(*dbinfo)
    db.start()
    print db.query("SELECT *FROM table")