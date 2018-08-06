# -*- coding: utf-8 -*-
# @Date    : 2018-08-02 12:57:48
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

import os
# 6. 写函数，函数接收四个参数分别是:姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这 四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中
def append(name,age,grade,sex='male'):
    f = open('student_msg.txt','a')
    f.write(name+','+sex+','+age+','+grade + '\n')
    f.close
    return f

# print append('姓名','性别','年龄','学历')

# 7. 对第6题升级:支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
import sys
def system():
    while True:
        raw = raw_input(u'请分别输入姓名,性别（男、女）年龄,学历,(空格隔开):')
        if raw == 'q' or raw == 'Q':
            sys.exit(1)
        print raw
        name,sex,age,grade = raw.strip().split(' ')

        if sex=='female':
            append(name,age,grade,sex)
        else:
            append(name,age,grade)

if __name__ == '__main__':
    system()
