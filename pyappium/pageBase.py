#coding:utf-8

#maojm
#2017/7/26
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class pageBase(object):
	''' 每个页面类的基类，定义操作页面的基本通用方法'''
	def __init__(self,driver):
		self.driver = driver

	def waitAndClick(self,elem,waittime=30):
		driver = self.driver
		WebDriverWait(driver,waittime).until(lambda driver: driver.find_element(*elem).is_displayed())
		self.driver.find_element(*elem).click()
		return self.driver
		return self

	def clickText(self,text,waittime=30):
		elem = (MobileBy.ANDROID_UIAUTOMATOR,u'new UiSelector().text("{}")'.format(text))
		self.waitAndClick(elem,waittime)
		return self

	def getContexts(self):
		print self.driver.contexts
		return self.driver.contexts

	def currentContext(self):
		print self.driver.contexts
		return self.driver.contexts

	def swipeUp(times,duration):
		elem = self.driver.find_element_by_xpath('//android.widget.FrameLayout')
		size = elem.size
		print size
		return self