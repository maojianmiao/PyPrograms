#coding:utf-8

import xlrd
import xlwt
import datetime
import time

def setStyle(name,height,bold=False):
	style = xlwt.XFStyle()

	font = xlwt.Font()

	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height

	style.font = font

	return style

def writeSheet():
	f = xlwt.Workbook()

	sheet1 = f.add_sheet('sheet',cell_overwrite_ok=True)
	row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
	column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
	status = [u'预订',u'出票',u'退票',u'业务小计']

	for i in range(0,len(row0)):
		sheet1.write(0,i,row0[i],setStyle('Times New Roman',220,True))

	i , j = 1, 0

	while i < 4*len(column0) and j <len(column0):
		sheet1.write_merge(i,i+3,0,0,column0[j],setStyle('Arial',220,True))
		sheet1.write_merge(i,i+3,7,7)
		i += 4
		j +=1

	i = 0
	while i < 4*len(column0):
		for j in xrange(0,len(status)):
			sheet1.write(i+j+1,1,status[j])
		i += 4

	f.save('demo.xls')
writeSheet()