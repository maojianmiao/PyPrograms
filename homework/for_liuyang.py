# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 21:33:12

'''
    有个日志debug.log, 写个程序分别统计2018-04-01 23:59.59 - 2018-04-02 23:59.59响应时间在0-100ms和500-200ms的进程个数。
    日志格式为：
    info: 2018-04-02 10:30.59   [20ms]  xxxx
    warning: 2018-04-02 10:30.23    [100ms] xxxx
    error: 2018-04-02 20:12.40  [200ms] xxx
    ..........................................
'''

import re
def paseLog(log):

    time_bottom = '2018-04-01 23:59.59'
    time_top = '2018-04-02 23:59.59'

    count_low = 0
    count_high = 0

    with open(log, 'rb') as f:
        for i in f:
            #re.MatchObject类
            time_obj = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}.\d{2}',i)
            res_obj = re.search('\[(\d+)ms\]',i)
            #如果没有匹配到时间或响应时间，则跳过这行
            if not time_obj or not res_obj:
                continue
            time = time_obj.group()
            res_time = int(res_obj.group(1))

            if time > time_bottom and time < time_top:
                if res_time >= 0 and  res_time <= 100:
                    count_low += 1

                if res_time >=200 and res_time <= 500:
                    count_high += 1


        print 'count 0-100ms: {}, count 200-500ms: {}'.format(count_low, count_high)