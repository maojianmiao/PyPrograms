#coding:utf-8

import json
import time
from datetime import datetime
import re

a = '2016-11-18 16:38:20'

def getIntTime(strtime):
	return time.mktime(time.strptime(strtime, '%Y-%m-%d %H:%M:%S'))


def group(originFile,outputJson=None):
	groupDict = {}

	with open(originFile,'rb') as f:
		for line in f:
			itemspaceid = getId(line)
			if not itemspaceid:
				continue
			
			if itemspaceid in groupDict.keys():
				groupDict[itemspaceid].append(line)
			
			else:
				groupDict[itemspaceid] = [line]
	for i in groupDict:
		groupDict[i].sort()
	with open('myjson.json','wb') as fb:
		json.dump(groupDict,fb,indent=4)
	return groupDict			

def getId(line):
	a = re.search('(apid\=beans_(\d{5})|itemspaceid\=(\d{5}))',line)
	if not a:
		return None
	return a.group(2)

d = group('output_result.txt')
print d['10103']