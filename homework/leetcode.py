#coding:utf-8
#
from dataStruct import *
from Queue import Queue

def ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
def merge(a,b,c):
    i,j,k = 0,0,0
    ra = len(a) - 1
    rb = len(b) - 1

    while i <= ra and j <= rb:
        if a[i]<=a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    while i <= ra:
        c.append(a[i])
        i += 1
    
    while j <=rb:
        c.append(b[j])
        j += 1
#zigzag
def convert(s, numRows):
    if numRows==1: return s
    rows=[[] for i in range(numRows)]
    k=2*numRows-2
    for i,ch in enumerate(s):
        r=min(i%k,k-i%k)
        rows[r].append(ch)
    str=''
    for row in rows:
        str+=''.join(row)
    return str
#TWOSUM
def addTwo(l1,l2):
    carry = 0
    if (l1.val +l2.val) >= 10:
        #print l1.val + l2.val
        carry = 1

    l1.val = (l1.val +l2.val)%10
    head = l1

    while l1.next and l2.next:
        #print carry
        a= l1.next.val + l2.next.val + carry

        l1.next.val =a % 10
        #print l1.next.val
        if a >=10:
            carry = 1
        else:
            carry = 0
        l1 = l1.next
        l2 = l2.next

    if not l1.next and l2.next:
        l2.next.val +=carry
        l1.next = l2.next
        carry = 0

    if not l2.next and l1.next:
        l1.next.val =l1.next.val + carry
        carry = 0

    if carry == 1:
        l1.next = LinkNode(1)

    return head
#longest substring
def lo(s):

    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    T = [1] * len(s)
    l = len(s)

    for i in range(1,len(s)):
        if s[i] in s[i-T[i - 1]:i]:
            T[i] = T[i-1] - s[i - T[i - 1]:i].index(s[i])
            print 'TI:',i,T[i]
        else:
            T[i] = T[i-1] + 1
            print 'TI:',i,T[i]
#对数
def pow(x,n):

    loop = abs(n)
    multipy = x

    if loop==0:
        return 1
    elif loop == 1:
        multipy = x
    else:   
        for i in xrange(loop-1):
            print i
            multipy *=x
    
    return multipy if n>0 else 1/multipy


def reverseInt(x):
	negetive = False
	if x < 0:
		x = -x
		negetive = True

	numlist = []
	while x>0:
		numlist.append(x % 10)
		x = x/10
	
	num = 0
	l = len(numlist)
	for i in xrange(l):
		num += numlist[i] * (10**(l - i - 1))
	
	if num>2147483647 or num<-2147483648:
		return 0
	
	return -num if negetive else num

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mergeList = ListNode(None)
        head = mergeList
        
        while l1 and l2:
            if l1.val < l2.val:
                mergeList.val = l1.val
                l1 = l1.next
            else:
                mergeList.val = l2.val
                l2 = l2.next
            
            mergeList.next = ListNode(None)
            mergeList = mergeList.next
        
        if l1:
        	mergeList.val = l1.val
        	if l1.next:
        		mergeList.next = l1.next

        while l2:
        	mergeList.val = l2.val
        	if l2.next:
        		mergeList.next = l2.next
        
        return head

class Solution11(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in xrange(len(nums)-2):
            if i==0 or (i>0 and (nums[i] != nums[i-1])):
            	print i,nums[i]
                lo = i+1
                hi = len(nums) - 1
                sum = 0 - nums[i]
                
                while lo<hi:
                    #print hi
                    if (nums[lo] + nums[hi]) == sum:
                        res.append([nums[i],nums[lo],nums[hi]])
                        #print [nums[i],nums[lo],nums[hi]]
                        
                        while lo<hi and (nums[lo] == nums[lo+1]):
                            lo +=1
                        while lo<hi and (nums[hi] == nums[hi-1]):
                            hi -=1
                        
                        lo += 1
                        hi -= 1
                        #print 'loop'
                    elif nums[lo] + nums[hi] < sum:
                        lo += 1
                    else:
                        hi -= 1
        return res

def apporch(nums,target):
	l,r = 0, len(nums) - 1

	if nums[l]>= target:
		return l
	if nums[r]<= target:
		return r

	while l<=r:
		m = (l + r) / 2
		if nums[m] == target:
			return m
		elif nums[m] <target:
			l = m + 1
		else:
			r = m - 1
	
	if abs(nums[l] - target) < abs(nums[r] - target):
		return l
	else:
		return r 

def threesum(nums,target):
	nums.sort()
	res = None

	
	for i in xrange(len(nums) - 2):
		for j in xrange(i+1,len(nums)-1):
			last = None
			for k in xrange(j+1,len(nums)):
				if (nums[i] + nums[j] + nums[k]) == target:
					return target

				elif (nums[i] + nums[j] + nums[k]) < target:
					last = nums[i] + nums[j] + nums[k]

				elif (nums[i] + nums[j] + nums[k]) > target:
					if last == None:
						last = nums[i] + nums[j] + nums[k]
						continue
					elif abs(nums[i] + nums[j] + nums[k] - target)>abs(last-target):
						continue
					else:
						last = nums[i] + nums[j] + nums[k]
						continue

			if res == None:
				res = last
			elif abs(last -target)<abs(res - target):
				res = last
	return res
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = []
        
        for i in xrange(len(nums)-3):
            for j in xrange(i+1,len(nums)-2):
                lo= j+1
                hi = len(nums)-1
                while lo<hi:
                    if (nums[i] + nums[j] + nums[lo] + nums[hi]) == target:
                    	if sorted([nums[i],nums[j],nums[lo],nums[hi]]) not in res:
                        	res.append(sorted([nums[i],nums[j],nums[lo],nums[hi]]))
                        while lo<hi and (nums[hi] == nums[hi -1]):
                            hi -= 1
                        while lo<hi and (nums[lo] == nums[lo + 1]):
                            lo += 1
                        
                        hi -= 1
                        lo += 1
                    
                    elif nums[i] + nums[j] + nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1
        return res


class Solution3(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in xrange(len(nums)-3):
            if i==0 or (i>0 and (nums[i] != nums[i-1])):
            	s = target - nums[i]
            	threesum = self.threeSum(nums[i+1:],s)
            
            	print threesum
            	if threesum:
                	for sub in threesum:
                		sub.append(nums[i])
                    	res.append(sub)
                
        return res
        
    def threeSum(self,nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in xrange(len(nums)-2):
            if i==0 or (i>0 and (nums[i] != nums[i-1])):
                lo = i+1
                hi = len(nums) - 1
                sum = target - nums[i]
                
                while lo<hi:
                    if (nums[lo] + nums[hi]) == sum:
                        res.append([nums[i],nums[lo],nums[hi]])
                        while lo<hi and (nums[lo] == nums[lo+1]):
                            lo +=1
                        while lo<hi and (nums[hi] == nums[hi-1]):
                            hi -=1
                        
                        lo += 1
                        hi -= 1
                        
                    elif (nums[lo] + nums[hi]) < sum:
                        lo += 1
                    else:
                        hi -= 1
        return res

def romanToInt(s):
    num = 0
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    for i in xrange(len(s)):
        if i <len(s) -1 and roman[s[i]]<roman[s[i+1]]:
            num -= roman[s[i]]
        else:
            num += roman[s[i]]

    return num

def intToRoman(num):
    s = ''
    roman = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
                 ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                 ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                 ["","M","MM","MMM"]]
                 
    s += roman[3][(num /1000 %10)]
    s += roman[2][(num /100 %10)]
    s += roman[1][(num /10 %10)]
    s += roman[0][(num %10)]
        
    return s
#Longest Common Prefix
#Write a function to find the longest common prefix string amongst an array of strings.
def longestCommonPrefix(strs):
    prefix = ''

    if not strs:
        return ''

    stop = False

    for s in xrange(len(strs[0])):
        if stop:
            break
        for i in strs:
            if s>len(i)-1:
                stop = True
                break
            if strs[0][s] !=i[s]:
                stop = True
                break

        else:
            prefix += strs[0][s]

    return prefix
'''
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    if x<0:
        return False
    x = str(x)
        
    for i in xrange(len(x)/2 + 1):
        if x[i] != x[len(x)-1-i]:
            return False
        
    return True
'''

def remove(head,n):
    h = head

    count = 1
    while head.next:
         head = head.next
         count += 1
    print count
    head = h
    if count - n == 0:
        print 'here'
        return h.next

    for i in xrange(1,count - n+1):
        if i == count - n and h.next.next:
            h.next = h.next.next
        elif i == count - n and not h.next.next:
            h.next = None

        h = h.next

    return head
#链表倒置
def reverseNode(node):
    pre = None
    n = None

    while node:
        n = node.next
        node.next = pre
        pre = node
        node = n
    return pre

def recursionNode(node):
    if node.next ==None:
        return node

    pre = recursionNode(node.next)
    temp = node.next
    node.next = None
    return pre
#链表以k为长度分别倒置    
def reverseKnode(node,k):
    i = 0
    pre = None
    next = None
    while i<k:
        next = node.next
        node.next = pre
        pre = node

        if i==0:
            tail = pre
        
        node = next
        i += 1
    if node:
        tail.next = next

    return pre

#53. Maximum Subarray

def MaxSubarray(seq):
    maxSofar = seq[0]
    maxHere = seq[0]
    for item in seq[1:]:
        maxHere = max(maxHere + item,item)
        maxSofar = max(maxSofar,maxHere)

    return maxSofar

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        if m==0:
            nums1[:] = nums2
            return
        if n ==0:
            return
        i = j = 0
        
        while i<m and j<n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i,nums2[j])
                i += 1
                m += 1
                j += 1
            else:
                i += 1
        if j < n:
            nums1[:] += nums2[j:]
            
s = Solution()

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
s.merge(nums1, m, nums2, n)
print nums1