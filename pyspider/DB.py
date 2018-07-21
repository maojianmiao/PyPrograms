#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Apr 18, 2016

@author: maojianmiao
'''
import sqlite3

class DB():
	
	DBName = ''

	def __init__(self,name='D:\\Projects\\NewsSpider\\src\\Notes\\news.db'):
		self.DBName = name


	def connectDB(self):
		try:
			self.conn = sqlite3.connect(self.DBName)
			self.cur = self.conn.cursor()
		except Exception,e:
			print '连接数据库失败，请检查网络和提供的信息是否正确'
	#query search
	def querySearch(self,query):
		contents = self.cur.execute(query).fetchall()
		if contents:
			for i in contents:
				yield i
	#query insert delete update or other
	def queryCommit(self,query):
		self.cur.execute(query)
		self.conn.commit()

	def close(self):
		self.conn.close()

mydb = DB()
mydb.connectDB()

datas = mydb.querySearch("SELECT Link FROM Topic WHERE ID=1231231231")
for i in  datas:
	print i

mydb.close()