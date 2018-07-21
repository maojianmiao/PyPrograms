#coding:utf-8

#maojm
#2017/8/10

import sys
sys.path.append(r'D:\Projects\appium')
from pageBase import pageBase
from appium.webdriver.common.mobileby import MobileBy


class launchPage(pageBase):
	def __init__(self,driver):
		self.driver = driver

	def launchApp(self):
		self.driver.find_element_by_android_uiautomator(u'new UiSelector().text("魂斗罗:归来")').click()
		#self.clickText(launchPageElems.launchIcon)
		return self

class launchPageElems(object):
	launchIcon = u'魂斗罗:归来'
