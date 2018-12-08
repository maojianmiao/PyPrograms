# -*- coding: utf-8 -*-
# @Date    : 2018-11-27 20:30:00
# @Author  : maojianmiao
# @Link    : http://example.org
# @Version : $Id$

import os
from base import mysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class dbBackup(mysql):
    def __init__(self,host, user, passwd, db, port=3306):
        super(dbBackup,self).__init__(host, user, passwd, db, port)
        self.start()

    def backup(self,query,filename):
        items = self.queryDicts(query)
        self.close()
        with open(filename,'wb') as f:
            if not items:
                return
            for key in items[0].keys():
                f.write(u'{}    '.format(key))
            f.write('\n')
            print items[0]
            for item in items:
                try:
                    for item_key in item.keys():
                        f.write(u'{}    '.format(item.get(item_key)))
                    f.write('\n')
                except Exception,e:
                    print '写入失败',e
                    print item.get(item_key)
