# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 23:32:04
# @Author  : linyuling
# @Version : $Id$
# @Notes   : 
import logging
import logging.handlers
import time
def test_log():
    logging.info("Hey")


def initLogger(pathname):
    """
    同时输出到控制台和文件
    """
    fmt = "[%(asctime)s %(levelname)s] [%(filename)s:%(lineno)d] [%(processName)s:%(process)s] [%(threadName)s:%(thread)s] %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level=logging.INFO,format=fmt,datefmt=datefmt)
    formatter = logging.Formatter(fmt,datefmt="%Y-%m-%d %H:%M:%S")
    file_handler = logging.handlers.TimedRotatingFileHandler(filename=pathname, when='D', interval=1, backupCount=5)
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logging.getLogger('').addHandler(file_handler)

def selfLogger(pathname):
    fmt = "[%(asctime)s %(levelname)s] [%(filename)s:%(lineno)d] [%(processName)s:%(process)s] [%(threadName)s:%(thread)s] %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt,datefmt=datefmt)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.handlers.TimedRotatingFileHandler(pathname, when='D', interval=1, backupCount=5)
    file_handler.suffix = '%Y-%m-%d'
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    return logger

if __name__ == "__main__":
    ####logging setting：同时输出到文件和控制台
    name = 'D:/test/test.log'
    initLogger(name)
    while True:
        time.sleep(1)
        test_log()
    #l = selfLogger("logger")
    #l.info("hello aaa")