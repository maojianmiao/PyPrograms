#coding:utf-8

#testcase

from testBase import testBase
from selenium.webdriver.support.ui import WebDriverWait
from pages.launchPage import launchPage
import time
dr = testBase.getHomeDriver()
page = launchPage(dr)
page.launchApp().swipeUp(1,2)