# -*- coding: utf-8 -*-
# @Date    : 2018-05-26 20:55:17
# @Author  : maojianmiao
# @Version : $Id$
# @Notes   : 

"""
大家好，我是kevin。

我们的基础课更难的知识点已经全部讲完。接下来，是两道应用题。这两道应用题，多多少少都有些难度。第一道是文本题，第二道则是小游戏题。前者考知识点，后者考逻辑。前者偏坑爹（难），后者偏有趣（更难^_^），这两道应用题，会给大家足够的时间去思考，总结与回顾。

第一道题，是一道文本题。文件夹里有一个twitter数据挖掘的片段，每一行则是一个tweets（微博），里面有该微博的相关字段信息。

对应字段如下（每一个逗号分隔的，“”内的，则是字段的详细信息。空白则代表没有。）：

bid    消息ID 
uid     用户ID 
username 用户名  
ugrade 用户等级字段 
content(text) 微博内容
img(message包含图片链接) 
created_at 微博发布时间 
source(来源)
rt_num, 转发数 
cm_num, 评论数 
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级 
rt_content, 转发内容 
rt_img, 转发内容所涉及图片 
src_rt_num, 源微博回复数 
src_cm_num, 源微博评论数 
gender,(用户性别) 
rt_mid（转发mid） 
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags 
ats  @谁 
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL 
rt_v_url 转发URL 


twitter文本附件的排序格式如下

fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url


而童鞋们，则需要利用自己已经掌握的知识，对其进行一个基本的文本分析。


注意：请用utf-8格式打开此文件。

要求如下：

1.该文本里，有多少个用户。（要求：输出为一个整数。）

2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）

6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 

8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）

14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）

测试文件：../res/twitter.txt
"""
import chardet
import os
#获取行内第n个元素的值
def getValue(line, position):
    l = line.split('","') #推特内容里面可能有逗号所以用","做分隔符，把干扰可能性降到最小
    #print len(l)
    return l[position].strip('"')
#1.该文本里，有多少个用户。（要求：输出为一个整数。）
def userCount(filename):
    uids = set() #存储各个uid，集合无重复
    with open(filename,'rb') as f:
        for line in f:
            if not line:
                continue
            uid = getValue(line,1)
            uids.add(uid)

    return len(uids)

#2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
def usersName(filename):
    names = set() #存储各个用户名，集合无重复
    with open(filename,'rb') as f:
        for line in f:
            if not line:
                continue
            tmp = getValue(line,2)
            names.add(tmp)

    return list(names)

#3.该文本里，有多少个2012年11月发布的tweets。 
def getNovTweetsCount(filename):
    start = "2012-11-01 00:00:00"
    end = "2012-12-01 00:00:00"
    count = 0
    with open(filename,'rb') as f:
        for line in f:
            if not line:
                continue
            tmp = getValue(line,6)
            #筛选11月区间内的微博
            if tmp > start and tmp< end:
                count += 1
    return count

#4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
def getDates(filename):
    s = set()
    with open(filename,'rb') as f:
        for line in f:
            if not line:
                continue
            tmp = getValue(line,6)
            if tmp:
                s.add(tmp)
    return list(s)
#5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
def getMostHour(filename):
    l = []
    
    with open(filename,'rb') as f:
        for line in f:
            if not line:
                continue
            tmp = getValue(line,6)
            if tmp:
                l.append(tmp)
    l.sort() #排序
    lagestCount = 1
    largestHour = l[0]
    pivot = l[0]
    current = 1
    for i in xrange(1,len(l)):
        if l[i][0:13] == pivot[0:13]: #匹配小时相等的日期比如2012-11-04 10:11:59和2012-11-04 10:22:22
        #前13位为2012-11-04 10相同，则是一个小时内的
            current += 1
        else:
            largestHour = pivot
            pivot = l[i]
            lagestCount = current
            current = 1
    print largestHour
    return lagestCount

#6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
def getUserByDay(filename):
    current = {}#数据{time1:{name1:count,name2:count},time2:{...},...}

    with open(filename,'rb') as f:
        for line in f:
            t = getValue(line, 6)[:10] #日期的天维度
            #uid = getValue(line, 1)
            name = getValue(line, 2)

            if t in current:
                if name in current[t]:
                    current[t][name] += 1
                else:
                    current[t][name] = 1
            else:
                current[t] = {name:1}
    for k,v in current.items():
        l = v.items()
        l.sort(lambda x,y:cmp(x[1],y[1]),reverse=True)
        current[k] = l[0][0]
    
    return current
#7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 
def getFrequencyDay(filename, date):
    result = []
    for i in xrange(24):
        result.append([i + 1,0]) #初始化存储列表
    print result
    print len(result)
    with open(filename,'rb') as f:
        for line in f:
            t = getValue(line,6)
            if t.startswith(date):
                try:
                    result[int(t[11:13])][1] += 1
                except Exception,e:
                    print e
    return result
#8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
def countSource(filename):
    d = {}
    with open(filename,'rb') as f:
        for line in f:
            src = getValue(line,7)
            if src in d:
                d[src] += 1
            else:
                d[src] = 1

    return d.items()

#9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
def countUrl(filename,url):
    count = 0
    with open(filename,'rb') as f:
        for line in f:
            quoteUrl = getValue(line,-1)
            #print quoteUrl
            if quoteUrl.startswith(url):
                count += 1

    return count
#10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
def countRt(filename,uid):
    count = 0
    with open(filename,'rb') as f:
        for line in f:
            quoteUrl = getValue(line,10) #转发微博uid
            current = getValue(line,1)
            #print quoteUrl
            if quoteUrl and current == uid:
                count += 1
    return count

#11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
def getMostTweets(filename,*uids):
    if not uids:
        return

    result = {}
    with open(filename,'rb') as f:
        for line in f:
            current = getValue(line,1)
            #print quoteUrl
            if current in uids:
                if current in result:
                    result[current] += 1
                else:
                    result[current] = 1

    l = result.items()
    l.sort(lambda x,y:cmp(x[1],y[1]),reverse=True)
    print l
    return l[0][0]

#12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
def getLongestTweetUser(filename):
    largest = 0
    uid = ''
    with open(filename,'rb') as f:
        for line in f:
            current = getValue(line,1)
            length= len(getValue(line,4))
            #print length
            if length >largest:
                largest = length
                uid = current
            #print quoteUrl
    print 'uid: %s, length: %s' % (uid, largest)
    return uid

#13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
def getMostLikeRtUser(filename):
    result = {}
    with open(filename,'rb') as f:
        for line in f:
            current = getValue(line,1)
            rturl = getValue(line,-1)
            if current in result:
                result[current] += 1
            else:
                result[current] = 1
    #[(uid1,count),(uid2,count)]
    l = result.items()
    l.sort(lambda x,y:cmp(x[1],y[1]),reverse=True) #按照元组的第二个元素大小排序
    #print l
    print 'uid: %s, count: %s' % l[0]
    return l[0][0]
#14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
def getMostTweetUserEleven(filename):
    result = {}
    with open(filename,'rb') as f:
        for line in f:
            uid = getValue(line,1)
            t = getValue(line,6)
            if t[11:13] == '11':
                if uid in result:
                    result[uid] += 1
                else:
                    result[uid] = 1

    #[(uid1,count),(uid2,count)]
    l = result.items()
    l.sort(lambda x,y:cmp(x[1],y[1]),reverse=True) #按照元组的第二个元素大小排序
    print 'uid: %s, count: %s' % l[0]
    return l[0][0]

#15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
def getMostRtUser(filename):
    result = {}
    with open(filename,'rb') as f:
        for line in f:
            rtuid = getValue(line,10)
            if not rtuid:
                continue
            if rtuid in result:
                result[rtuid] += 1
            else:
                result[rtuid] = 1
    
    #[(uid1,count),(uid2,count)]
    l = result.items()
    l.sort(lambda x,y:cmp(x[1],y[1]),reverse=True) #按照元组的第二个元素大小排序
    print 'uid: %s, count: %s' % l[0]
    return l[0][0]

if __name__ == '__main__':
    filename = os.path.abspath('../res') + '\\twitter.txt'
    #print userCount(filename)
    #a  = usersName(filename)
    #print getNovTweetsCount(filename)
    #print getDates(filename)
    #print getMostHour(filename)
    #print getUserByDay(filename)
    #print getFrequencyDay(filename,'2012-11-03')
    #print countSource(filename)
    #print countUrl(filename,"https://twitter.com/umiushi_no_uta")
    #print countRt(filename,'573638104')
    #print getMostTweets(filename,'573638104','426736841')
    #print getLongestTweetUser(filename)
    #print getMostLikeRtUser(filename)
    #print getMostTweetUserEleven(filename)
    print getMostRtUser(filename)