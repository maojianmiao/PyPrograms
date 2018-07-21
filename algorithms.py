#coding:utf-8
'''
Created on 2016-7-11

@author: jm
'''
import hashlib
import time
from Queue import Queue
import daily
''' 
    有N个台阶，每次只能走1,2步，求有多少走法
'''
def steps(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        return steps(N-1) + steps(N-2)

#计算大文件的MD5值
def md5sum(filename,size=64 * 1024):
    with open(filename,'rb') as f:
        MD5 = hashlib.md5()
        #completed = 0
        while True:
            data = f.read(size)
            if not data:
                break
            MD5.update(data)
            #completed += size/(1024)
            #print completed
        return MD5.hexdigest()
    
def fib(n):
    #if fn[n] >1:
    #    return fn[n]

    if n==2 or n==1:

        return 1

    num = fib(n-1) + fib(n - 2)
    
    #fn[n] = num
    return num

def fib2(n):
    a = 0
    b = i = 1
    while(i<n):
        num = a + b
        a = b
        b = num
        i +=1
        print a,
        
def myReversed(list_a):
    i = 0;
    j = len(list_a) - 1
    while i < j:
        tmp = list_a[i]
        list_a[i] = list_a[j]
        list_a[j] = tmp
        i +=1
        j -=1
    return list_a

#冒泡排序
def bubble(l):
    for i in range(len(l)-1,0,-1):
        for j in range(0,i):
            if l[j] > l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp

#快排       
def quickSort(seq,l,r):
    
    if l < r:
        pivot = seq[l]
        p = l

        for i in xrange(l+1,r+1):
            if seq[i]<pivot: 
                seq[p] = seq[i]
                p += 1
                seq[i] = seq[p]
            
        seq[p] = pivot
        
        quickSort(seq, l, p-1)
        quickSort(seq, p+1, r)
        
#插入排序
def insert(seq):
    for i in xrange(1,len(seq)):
        j = i
        temp = seq[i]
        while j>0 and temp<seq[j-1]:
            seq[j] = seq[j - 1]
            j -= 1
            
        seq[j] = temp
#选择排序      
def choose(seq):
    for i in xrange(0,len(seq)):
        p = i
        #找出最小值
        for s in xrange(i+1,len(seq)):
            if seq[s]<seq[p]:
                p = s
        #交换       
        if (p != i):
            tmp = seq[i]
            seq[i] = seq[p]
            seq[p] = tmp
            
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
#对双位数进行基数排序
def radix(seq, k):
    digitgroup = []
    group = 10

    for i in xrange(group):
        digitgroup.append(Queue())
    j = 1
    for times in xrange(k):
        for i in xrange(len(seq)):
            temp = seq[i]
            digit = (temp % (j*10)) / j
            digitgroup[digit].put(seq[i])

        j *= 10

        num = 0
        for i in xrange(group):
            while not digitgroup[i].empty():
                seq[num] = digitgroup[i].get()
                num += 1 

#希腊数学家埃拉托色尼算法
def primeEratosthense(n):
    p = range(2,n+1)

    i = 2
    while i*i<=n:
        if i in p:
            mult = 2 *i
            while mult<=n:
                try:
                    p.remove(mult)
                except ValueError,e:
                    pass
                mult += i
        i += 1
    return p
#判断文件夹是否为空
def isEmptyDir(dirpath):
    if not dirpath.endswith('\\'):
        dirpath = dirpath + '\\'
            
    dirpath = dirpath.decode() + '*'
        #print dirpath
        #print glob.glob(dirpath)
    if glob.glob(dirpath):
        return False
    else:
        return True
    
#删除空文件夹
def delEmptyDirs(dirpath):
    if not dirpath.endswith('\\'):
        dirpath = dirpath + '\\'    
    items = glob.glob(dirpath.decode() + '*')
    for item in items:
        if os.path.isdir(item):
            if isEmptyDir(item):
                os.rmdir(item)
                print 'remove %s from your PC' % item
            else:
                delEmptyDirs(item)
        else:
            continue
        #wukong.delEmptyDirs(dirpath)
#从配置文件夹中获取一个变量字典
#配置文件夹格式：
#var1=1
#var2=2        
def getDict(text):
    List = text.split()
    d = dict()
    for i in List:
        d[i.split('=')[0]] = i.split('=')[1]
    return d
	
class Solution_count(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        if n == 2:
            return '11'
        last = self.countAndSay(n - 1)
        
        result = ''
        count = 1
        for i in range(len(last) - 1):
            if last[i] == last[i + 1]:
                count += 1
                continue
            
            else:
                result += str(count) + str(last[i])
                print result
                count = 1
                continue
        
        if len(last)>=2 and last[-1] != last[-2]:
            result += '1' + str(last[-1])
        
        return result

#fn = [1] * 45
print fib(40)
