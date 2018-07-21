#coding:utf-8

import pymssql
import _mssql
import socket
import decimal
import uuid
import os
import sys
sys.path.append(r'C:\Python27\Lib\site-packages\pywin32_system32\\')

class MSSQL:
    def __init__(self,host,user,pwd):
        self.host = host
        self.user = user
        self.pwd = pwd

    def GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            self.cur = cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        """
        #cur = self.__GetConnect()
        self.cur.execute(sql)
        resList = self.cur.fetchall()

        #查询完毕后必须关闭连接
        #self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        """
        self.cur.execute(sql)
        self.conn.commit()

    
    def close(self):
        self.conn.close()
        
##判断
def isServer(res):
    if len(res) == 2:
        return 2
    elif '***' in res[0][0]:
        return 1 #client
    else:
        return 0 #Server

def getDict(text):
    List = text.split('\r\n')
    d = dict()
    for i in List:
        d[i.split('=')[0]] = i.split('=')[1]
    return d
        
def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3'    ##创建SQL连接 

    ms = MSSQL(host=varDict['sqlhost'],user=varDict['sqluser'],pwd=varDict['sqlpwd'])
    ms.GetConnect()
    
    for i in f.read().split('\r\n'):
        sql = "select *** from *** where ***=(select top 1 *** from*** where *** like '*%{0}%{1}')".format(i[8:12]+ ':'+i[12:19], varDict['arch'])
        print sql
        resList = ms.ExecQuery(sql)
        vali = isServer(resList)
        if vali == 2:
            cs.write(i + '\n')
        elif vali == 1:
            c.write(i + '\n')
        else:
            s.write(i + '\n')
    #关闭数据库连接
    ms.close()
    #关闭文件
    f.close()
    cs.close()
    s.close()
    c.close()

###################
vartext = open('Option.ini','rb').read()
varDict = getDict(vartext)
########################-configurations-#########################

##输入PLF or PLS text
try:
    os.makedirs('Result')
except Exception,e:
    print 'Folder is exist'

f = open(varDict['inputfile'],'rb')
##输出到当前目录
cs = open(r'***.txt','w')
s = open(r'***.txt','w')
c = open(r'***.txt','w')
###########################-Main-################################
main()

print 'over'
