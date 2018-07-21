'''
Created on May 30, 2016

@author: lauvey
'''
import unittest
import sys

class Test(unittest.TestCase):

    def test_importSpider(self):
        sys.path.append(r'D:\Projects\NewsSpider\src')
        import spider


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()