#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Jun 15, 2016

@author: maojianmiao
'''
class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val
    
class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print m.x
m.x = 20
print m.x
print m.y