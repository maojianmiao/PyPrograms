#coding:utf-8
from distutils.core import setup
import py2exe
import sys
sys.path.append(r'C:\Python27\Lib\site-packages\pywin32_system32\\')


setup(console=['mssql.py'])