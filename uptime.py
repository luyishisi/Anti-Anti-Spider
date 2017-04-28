#coding:utf-8
import os
import time
print 'begin'
pwd = r'/Users/ly/aiwen/doc/02.工作计划/工作日志/'
listfile = os.listdir(pwd)

for i in listfile:
    print i

    statinfo = os.stat(pwd+i)
    print time.localtime(statinfo.st_mtime)
    #print time.strftime(statinfo)
    break
#
#
# statinfo=os.stat(pwd+r"")
# print statinfo
# print statinfo.st_mtime

# print time.localtime(statinfo.st_ctime)
