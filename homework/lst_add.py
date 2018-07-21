#!c:\python27\python.exe
#coding:utf-8
#BY:maojm

from ftplib import FTP
import os
import shutil
import time
import glob

#langs = ['da','de','es','fi','fr','it','ja','ko','nl','no','pt','ru','sv','zh_CN','zh_TW','cs','hu','pl','pt_PT','zh_HK']

archs = ['x86','x86_64']
langs = ['de','fu','po']

def main():
	#get all LST
	print 'Downloading lst files'
	for arch in archs:
		for lang in langs:
			getLangLst(arch,lang)

	#backup all lst files
	print 'Backuping'
	backupLstsTo('c:\\backuplst')

	#add new patches to lst
	for arch in archs:
		for lang in langs:
			changeLst(arch,lang)

	#upload pls and plp to CDN!!
	print 'uploading pls and plp to CDN!!'
	files = getFiles('forupload')
	if files:
		for f in files:
			for arch in archs:
				for lang in langs:
					putLangFile(arch,lang,f[10:])

	#upload all lst files to CDN
	print 'upload all lst files to CDN'
	for arch in archs:
		for lang in langs:
			putLangFile(arch,lang,'apps.lst')


def getLangLst(arch,lang):
	try:
		myftp = FTP('172.27.52.36','administrator','123123')
		myftp.cwd('/windows/' + arch + '/' + lang)
		print 'Connect successfully.'
	except Exception,e:
		print 'Connect error, please check your network or ftp info. '
		print 'Cannot navigate to {}/{}'.format(arch,lang)
		print e

	
	#print 'Navigate to {}/{}'.format(arch,lang)
	myftp.retrbinary('RETR apps.lst',writeLst('windowslst\\' + arch + '\\' + lang).write)
	print 'Lst is stored in {}/{}/apps.lst'.format(arch,lang)
	myftp.close()

def putLangFile(arch,lang,filename):
	try:
		myftp = FTP('172.27.52.36','administrator','123123')
		myftp.cwd('/windows/' + arch + '/' + lang)
		print 'connect successfully.'
	except Exception,e:
		print 'connect error, please check your network or ftp info. '
		print 'Cannot navigate to {}/{}'.format(arch,lang)
		print e

	
	if filename == 'apps.lst':
		myftp.storbinary('STOR apps.lst',open('windowslst\\' + arch + '\\' + lang + '\\' + filename,'rb'))

	else:
		myftp.storbinary('STOR {}'.format(filename),open('forupload\\' + filename,'rb'))

	myftp.close()

def backupLstsTo(path):
	if not os.path.exists(path):
		os.makedirs(path)

	timename = time.strftime('%Y%m%d%H%M%S',time.localtime())
	shutil.copytree('windowslst',path + '\\' + timename)

def writeLst(path):
	if not os.path.exists(path):
		os.makedirs(path)

	return open(path + '\\apps.lst','wb')

def changeLst(arch,lang):
	addlst = open('forupload\\upload.txt','rb').read()
	langlst = open('windowslst\\' + arch + '\\' + lang + '\\' + 'apps.lst','ab')
	langlst.write(addlst)

def getFiles(path):
	pls = glob.glob('forupload\\*.pls')
	plp = glob.glob('forupload\\*plp')

	return pls + plp

def sortLst(filename):
	with open(filename,'rb') as f:
		items = f.readlines()
		items.sort(lambda x,y:cmp(x[34:],y[34:])) #跳过条目的md5值，根据文件名排序

	with open(filename,'wb') as f:
		for item in items:
			if item:
				f.write(item)

main()