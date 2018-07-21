# -*- coding: utf-8 -*-
# @Date    : 2018-02-14 23:27:08
# @Author  : maojianmiao
# @Version : $Id$
# @Notes   :

from __future__ import print_function

def collatz(number):

    if number % 2 == 0:
        result = number // 2
    else:
        result = 3*number + 1

    return result

def helpCollatz(num):
    if num == 1:
        print(1)
        return 1
    num = collatz(num)
    helpCollatz(num)

#输入列表输出字符串
def toString(seq):
    if not seq:
        return ''
    length = len(seq)

    result = str(seq[0])
    for i in xrange(1, length):
        if i == length:
            return result
        if i + 1 == length:
            return result + ' and {}'.format(seq[i])
        else:
            result += ', {}'.format(seq[i])
    return result

def printGrid(seq):
    for l in seq:
        for i in l:
            print(i,end=''),
        print()

if __name__ == '__main__':
    #a = ['1','2','3']
    #print toString(a)
    b = [['1','2','3',4],
         [1,2,3,4,],
         [1,2,3,4]]
    printGrid(b)
    