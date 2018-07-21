# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 23:32:04
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 
import logging

def test_log():
    logging.info("Hey")

if __name__ == "__main__":
    ####logging setting：同时输出到文件和控制台
    logging.basicConfig(filemode="w",filename="res/DEBUG.LOG",level=logging.INFO,format="%(asctime)s %(levelname)s: %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    test_log()