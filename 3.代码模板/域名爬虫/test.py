#coding:utf-8
import os,re,time,MySQLdb,MySQLdb.cursors,urllib2,random
from redis import Redis
import time

REDIS_HOST = '192.168.1.180'
REDIS_PORT = 6379
PASSWORD=''
r=Redis(host=REDIS_HOST, port=REDIS_PORT,password=PASSWORD)

i = 0
# for i in range(55677,100000):
#     print i
#     r.sadd('test', i)
print r.sismember('test',12341111)#
#print r.srandmember('test',1)

now_url =  r.srandmember('orgname',1);
print now_url

while 1:
    try:
        body = requests.get(now_url,timeout=10)
