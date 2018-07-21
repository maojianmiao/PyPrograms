#!c:\Python27\python.exe
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2016

@author: maojianmiao
'''
import pymssql

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
        return iter(resList)

    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        """
        self.cur.execute(sql)
        self.conn.commit()

    
    def close(self):
        self.conn.close()
        
#JUST FOR RHEL 5 OR 6 
def stripName(patchname):
    patchname = patchname[21:-5]
    removeElement=(' Important ',' Moderate ',' Critical ',' Low ',' security, bug fix, and enhancement ',' security and bug fix ',' security and enhancement ',
                   ' security ',' bug fix and enhancement ', ' bug fix ',' enhancement ', ' new package ',' update ',' new packages ')
    for i in removeElement:
        try:
            patchname = patchname.replace(i,' ')
        except Exception,e:
            print patchname
            print e
    return '%' + patchname.replace(' for ',' %for ')
    
def seqFile(filepath):
    f = open(filepath)
    data = f.read()
    f.close()
    return data.split('\n')

def querySupersede(patches,mysql,query):
    for n in patches:
        if n:
            supersede = None
            spname = None
            formatname = stripName(n)
            p = mysql.ExecQuery(query.format(formatname))
            nid = n[8:12] + ':' + n[12:17]
            #print nid
            try:
                while True:
                    patchinfo = p.next()
                    if nid in patchinfo[1]:
                        tmp = p.next()
                        supersede = str(tmp[0]).upper()
                        spname = str(tmp[1])
                        break
            except Exception:
                pass
            print n + ' SUPERSEDE: ', supersede
    mysql.close()
    
def main():
    patches = seqFile('plfz')
    mysql = MSSQL('','','')
    mysql.GetConnect()
    query = "SELECT PatchLink_UID,Bulletin_Name FROM PLUS.dbo.Bulletins WHERE Bulletin_Name NOT LIKE 'Detect%' AND \
    Bulletin_Name LIKE '{0}' ORDER BY Bulletin_Name DESC"      
    querySupersede(patches,mysql,query)  
    
main()
#print mysql.ExecQuery("select * from PLUS.dbo.Bulletins where Bulletin_Name not like 'Detect%' and Bulletin_Name like '%mod_wsgi %6 s% x86%' ORDER BY Bulletin_Name DESC")
