#coding:utf-8

import json
import glob
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
	这个脚本的功能是把百度文库的离线存储的许多Json文件，重新提取为一个txt文档。
	目前只支持生成TXT，有图片等其它文件格式并未打算支持。

	写这个脚本的原因是因为手机百度文库太难用了，很多资料也只有百度文库有，所以
	要把离线文件提取出来，到其它阅读器看。。	
'''
#快速排序，通过不带扩展名的文件名序号大小增序排列json文件。
def quicksortnum(seq,l,r):
	key = seq[l]
	i = l
	j = l

	while (i < r):
		for s in xrange(l+1,r+1):
			i = s
			print seq[i],key
			if int(seq[i][:-5]) < int(key[:-5]):
				seq[j] = seq[i]
				j +=1
				seq[i] = seq[j]

		seq[j] = key;

		quicksortnum(seq,l,j-1)
		quicksortnum(seq,j+1,r)

def main():
	outputFileName = 'waitforgotta.txt'
	print os.getcwd()
	f = open(outputFileName,'wb')

	#扫描当前目录下的json文件
	fl = glob.glob('*.json')

	quicksortnum(fl,0,len(fl)-1)
	
	for i in fl:
		with  open(i,'rb') as d:
			data = json.load(d)
			for s in data['parags']:
				f.write(s['c'] + '\r\n')

	f.close()

main()