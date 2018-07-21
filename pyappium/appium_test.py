#coding:utf-8

#appium

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import subprocess
from selenium.webdriver.common.proxy import Proxy




def test_launch():
	caps = {}

	caps['platformName'] = 'Android'
	caps['platformVersion'] = '4.4'
	#caps['deviceName'] = 'NX403A'
	caps['deviceName'] = '127.0.0.1:62001'
	#caps['appPackage'] = 'com.android.calculator2'
	#caps['appActivity'] = '.Calculator'
	#caps['app'] = 'd:\\SohuNewsClient_v5.8_20161130233958_test.apk'
	caps['appPackage'] = 'com.sohu.newsclient'
	caps['appActivity'] = '.app.NewsTabActivity'
	caps['udid'] = '127.0.0.1:62001'
	#host = 'http://10.2.145.236:4723/wd/hub'
	host = 'http://127.0.0.1:4723/wd/hub'
	driver = webdriver.Remote(host, caps)

	return driver

def waitAndClick(driver,elem,duration):
	WebDriverWait(driver,duration).until(lambda driver: driver.find_element(*elem).is_displayed())
def testscroll(driver):
	driver.find_element_by_id()
def test_clean_install():
	proxy = Proxy()
	proxy.http_proxy = 'localhost:8888'
	#proxy.proxy_type = {'ff_value': 1, 'string': 'MANUAL'}
	caps = {}
	caps['platformName'] = 'Android'
	caps['platformVersion'] = '4.4'
	#caps['deviceName'] = 'NX403A'
	caps['deviceName'] = 'Android Emulator'
	caps['app'] = 'd:\\SohuNewsClient_v5.8_20161130233958_test.apk'
	#caps['udid'] = 'NX403A'

	driver = webdriver.Remote('http://localhost:4723/wd/hub', caps, proxy=proxy)
	time.sleep(15)
	driver.swipe(250,1100,130,1100,200)
	time.sleep(1)
	driver.swipe(300,1100,130,1100,200)

def test_caculator():
	caps = {}

	caps['platformName'] = 'Android'
	caps['platformVersion'] = '4.4'
	#caps['deviceName'] = 'NX403A'
	caps['deviceName'] = 'Android Emulator'
	caps['appPackage'] = 'com.android.calculator2'
	caps['appActivity'] = '.Calculator'
	#caps['udid'] = 'NX403A'
	#caps['app'] = 'd:\\SohuNewsClient_v5.8_20161130233958_test.apk'
	#caps['appPackage'] = 'com.sohu.newsclient'
	#caps['appActivity'] = '.app.NewsTabActivity'
	
	driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
	driver.swipe(700,500,100,500)
	#driver.find_element_by_id('com.android.calculator2:id/del').click()
	#driver.find_element_by_id('com.android.calculator2:id/digit8').click()
	#driver.find_element_by_id('com.android.calculator2:id/mul').click()
	#driver.find_element_by_id('com.android.calculator2:id/digit9').click()
	#driver.find_element_by_id('com.android.calculator2:id/equal').click()

#test_launch()
#test_caculator()
#test_clean_install()
def release_port(port):
	#find pid by port
	cmdStr = 'netstat -ano|findstr "'+ str(port) + '" |findstr "LISTENING"'
	#res = os.system(cmdStr)
	res = subprocess.Popen(cmdStr,shell=True,stdout=subprocess.PIPE).communicate()[0]
	print res
	
	
	#kill process
	if res.strip() == '':
		print 'no pid to kill'
		return True
	else:
		pid = res.strip()[-6:].strip()
		cmdKillStr = 'tskill ' + str(pid)
		o = os.system(cmdKillStr)
		if int(o) == 0:
			print 'stop the program by pid successfully'
			return True
		else:
			print 'failed to stop the program'
			return False

def start_appium(port):
	release_port(port)
	appiumpath = r'C:\Program Files (x86)\Appium\node_modules\.bin'
	os.chdir(appiumpath)
	os.system('cmd.exe /k appium -a 127.0.0.1 -p {}'.format(port))

#comment = '//*[@text="我来说两句"]'
dr = test_launch()
elem = ('id','com.sohu.newsclient:id/negative_btn')
WebDriverWait(dr,30).until(lambda dr: dr.find_element(*elem).is_displayed())
elem = dr.find_element_by_id('com.sohu.newsclient:id/negative_btn')
print 'text:',elem.text
elem.click()


'''
#time.sleep(15)
#waitAndClick(dr,('xpath',u'//*[@text="要闻""]'),30)
#time.sleep(20)
dr.find_element_by_xpath(u'//*[@text="要闻"]').click()
#print dr.page_source
dr.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout[@index="6"]').click()
time.sleep(10)
print dr.page_source
elem = dr.find_element_by_xpath(comment)
dr.execute_script("mobile: scroll", {"direction": 'up', 'element': elem.id})
'''