#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：push_redis.py
#   版本：0.1
#   作者：luyi
#   日期：编写日期2016/12/6
#   语言：Python 2.7.x
#   操作：python push_redis.py
#   功能：请求妹子图网网页,将任务队列(url)放入redis队列中
#   环境: linux ubuntu 16.04  redis 部署在本机
#
#-------------------------------------------------------------------------
#完成通用爬虫，抓取一个页面队列中所有图片

import requests
import re
import time
from redis import Redis

headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

def download(url):
    '''给定一个图片的url,下载并保存到./pic/目录下'''
    try:
        r = requests.get(url,headers=headers,timeout = 50)
        name = int(time.time())
        f = open('./pic/'+str(name)+'.jpg','wb')
        f.write(r.content)
        f.close()
    except Exception,e:
        print Exception,":",e
        return -1

def list_img_url(url):
    try:
        r = requests.get(url, timeout = 50 , headers=headers)
        img_list = re.findall("http://pic.meizitu.com/wp-content/uploads/.*jpg",r.text)
        print img_list
        for i in img_list:
            print i
            download(i)
    except:
        pass

def get_big_img_url():
    r = Redis()
    print r.keys('*')
    while(1):
        try:
            url = r.lpop('meizitu')
            return_1 = download(url)
            if return_1 == -1:
                return -1
            time.sleep(1)
            print url
        except:
            print "请求求发送失败重试"
            time.sleep(10)
            continue
    return 0

def push_redis_list(num):
    r = Redis()
    print r.keys('*')
    for i in range(100):
        num = num+i;#抓取的取件仅在num+100--num+200之间
        url ='http://www.meizitu.com/a/'+ str(num) +'.html'
        img_url = requests.get(url,timeout=30)
        #print img_url.text
        #time.sleep(10)
        img_url_list = re.findall('http://pic.meizitu.com/wp-content/uploads/201.*.jpg',img_url.text)
        print img_url_list
        for temp_img_url in img_url_list:
            l = len(re.findall('limg',temp_img_url))
            #print l
            if(l == 0):
                print "url: ",temp_img_url
                r.lpush('meizitu',temp_img_url)
        print r.llen('meizitu')
    return 0

if __name__ == '__main__':
    url = 'http://www.meizitu.com/a/list_1_'
    print "begin"
    #push_redis_list(4100)#开启则加任务队列.其中的值请限制在5400以内。不过是用于计算页码的
    get_big_img_url()#开启则运行爬取任务

