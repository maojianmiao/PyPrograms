#coding:utf-8

import os
import subprocess
import glob


def createInit(path):
    result = []

    cmd = 'dir {} /b /a:d'.format(path)
    print cmd

    os.chdir(path)
    py = glob.glob('*.py')
    folder = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0]
    print repr(folder)
    folder = folder.split('\r\n')
    print folder

    with open(path + '\\' + '__init__.py', 'wb') as f:
        f.write('#coding:utf-8\n')

        for i in py:
            if not i:
                continue
            if i != '__init__.py':
                s = 'from {} import *\n'.format(i.replace('.py',''))
                #print s
                f.write(s)
                
        for d in folder:
            #print d
            if not d:
                continue
            s = 'import {}\n'.format(d.strip())
            print 's:',s
            f.write(s)

    for d in folder:
        if not d:
            continue
        print 'path:',path + '\\' + d
        createInit(path + '\\' + d)
        
    
if __name__=='__main__':
    path = r'D:\SVN\automation\Code\basefunction'
    createInit(path)
    path = r'D:\SVN\automation\Code\basefunction_v2'
    createInit(path)
