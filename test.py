#coding:utf-8
#maojm
#

import algorithms as AL 
import unittest

class testAlgorithms(unittest.TestCase):

	def test_md5sum(self):
		filename = r'd:\bob.apk'
		thismd5 = AL.md5sum(filename)

		self.assertEqual(thismd5.upper(),'CBE76AB838A51FDF6CD2C77AD221424F')

	def test_reverse(self):
		l = [7,1,2,3,4,5,6,7,8,9,2,1,2,111,1,1,1]
		l2 = [0]
		l3 = [0,0,0,0]

		lc = l[:]
		l2c = l2[:]
		l3c = l3[:]

		l.reverse()
		l2.reverse()
		l3.reverse()

		self.assertEqual(AL.myReversed(lc),l)
		self.assertEqual(AL.myReversed(l2c),l2)
		self.assertEqual(AL.myReversed(l3c),l3)
	
	def test_bubble(self):
		l = [2,3,4,1,4,5,6,7,2,34,5,1,111,111,1,1,123,4,23]
		l1 = [0]
		l2 = [0,0,0,0,0]
		l3 = [1,2,3,4,5,6,7,8,9,10]
		
		AL.bubble(l)
		AL.bubble(l1)
		AL.bubble(l2)
		AL.bubble(l3)

		self.assertEqual(l,sorted(l))
		self.assertEqual(l1,sorted(l1))
		self.assertEqual(l2,sorted(l2))
		self.assertEqual(l3,sorted(l3))
	
	def test_quicksort(self):
		l = [2,3,4,1,4,5,6,7,2,34,5,1,111,111,1,1,123,4,23]
		l1 = [0]
		l2 = [0,0,0,0,0]
		l3 = [1,2,3,4,5,6,7,8,9,10]
		
		AL.quickSort(l,0,len(l)-1)
		AL.quickSort(l1,0,len(l1)-1)
		AL.quickSort(l2,0,len(l2)-1)
		AL.quickSort(l3,0,len(l3)-1)
		
		self.assertEqual(l,sorted(l))
		self.assertEqual(l1,sorted(l1))
		self.assertEqual(l2,sorted(l2))
		self.assertEqual(l3,sorted(l3))
	
	def test_choose(self):
		l = [2,3,4,1,4,5,6,7,2,34,5,1,111,111,1,1,123,4,23]
		l1 = [0]
		l2 = [0,0,0,0,0]
		l3 = [1,2,3,4,5,6,7,8,9,10]
		
		AL.choose(l)
		AL.choose(l1)
		AL.choose(l2)
		AL.choose(l3)
		
		self.assertEqual(l,sorted(l))
		self.assertEqual(l1,sorted(l1))
		self.assertEqual(l2,sorted(l2))
		self.assertEqual(l3,sorted(l3))

	def test_insert(self):
		l = [2,3,4,1,4,5,6,7,2,34,5,1,111,111,1,1,123,4,23]
		l1 = [0]
		l2 = [0,0,0,0,0]
		l3 = [1,2,3,4,5,6,7,8,9,10]
		
		AL.insert(l)
		AL.insert(l1)
		AL.insert(l2)
		AL.insert(l3)
		
		self.assertEqual(l,sorted(l))
		self.assertEqual(l1,sorted(l1))
		self.assertEqual(l2,sorted(l2))
		self.assertEqual(l3,sorted(l3))	

def suite():
	tests = ['test_bubble','test_reverse','test_quicksort','test_choose','test_insert']
	mysuite = unittest.TestSuite(map(testAlgorithms,tests))

	return mysuite


#if __name__ == '__main__':
#	unittest.main()

#suite = unittest.TestLoader().loadTestsFromTestCase(testAlgorithms)
#unittest.TextTestRunner(verbosity=2).run(suite)
suite = suite()
unittest.TextTestRunner(verbosity=3).run(suite)