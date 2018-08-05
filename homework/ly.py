# -*- coding: utf-8 -*-
# @Date    : 2018-08-02 23:01:50
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 



def addArgs(*args):
    result = []
    for item in args:
        for i in item:
            result.append(i)
    return result

def stringArgs(*args):
    result = ''
    for item in args:
        result += '-'.join(map(str,item)) + '-'
    return result.strip('-')

def stringLink(args):
    return '-'.join(map(str,item))


if __name__ == "__main__":
    a = [1,2,3,4]
    b = (6,7,8,9)
    c = set(b)
    print stringArgs(a)