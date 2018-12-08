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


def accum(string):
    result = ''
    for i in xrange(len(string)):
        if i == 0:
            result = string[i].upper()
            continue
        current = string[i].upper() + string[i].lower() * i
        result += '-' + current
    return result

if __name__ == "__main__":
    s = 'abcdea'
    print accum(s)
