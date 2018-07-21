#coding:utf-8

#maojm
#2017/7/26

from appium import webdriver

class testBase(object):

	@staticmethod
	def getDriver():
		caps = {}

		caps['platformName'] = 'Android'
		caps['platformVersion'] = '4.4'
		#caps['deviceName'] = 'NX403A'
		caps['deviceName'] = '127.0.0.1:62001'
		caps['appPackage'] = 'com.android.calculator2'
		#caps['appActivity'] = '.Calculator'
		#caps['app'] = 'd:\\SohuNewsClient_v5.8_20161130233958_test.apk'
		caps['appPackage'] = 'com.sohu.newsclient'
		caps['appActivity'] = '.app.NewsTabActivity'
		caps['udid'] = '127.0.0.1:62001'
		#host = 'http://10.2.145.236:4723/wd/hub'
		host = 'http://127.0.0.1:4723/wd/hub'
		driver = webdriver.Remote(host, caps)

		return driver
	@staticmethod
	def getHomeDriver():
		caps = {}

		caps['platformName'] = 'Android'
		caps['platformVersion'] = '4.4'
		#caps['deviceName'] = 'NX403A'
		caps['deviceName'] = '127.0.0.1:62001'
		#caps['appPackage'] = 'com.android.calculator2'
		#caps['appActivity'] = '.Calculator'
		#caps['app'] = 'd:\\SohuNewsClient_v5.8_20161130233958_test.apk'
		caps['appPackage'] = 'com.vphone.launcher'
		caps['appActivity'] = 'Launcher'
		caps['udid'] = '127.0.0.1:62001'
		#host = 'http://10.2.145.236:4723/wd/hub'
		host = 'http://127.0.0.1:4723/wd/hub'
		driver = webdriver.Remote(host, caps)
	
		return driver