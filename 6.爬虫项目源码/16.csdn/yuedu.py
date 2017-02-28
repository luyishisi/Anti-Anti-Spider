#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：get_page_id.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2017/2/27
#   语言：Python 2.7.x
#   操作：python get_page_id.py
#   功能：给定用户名name，获取该用户所有已经发表的文章id
#-------------------------------------------------------------------------
import requests
import re,sys
from lxml import etree
import random,time



def  forge_headers(url,user_agent,ip):
    if len(user_agent ) < 10:
		user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
    headers = {
        'cache-control': "no-cache",
        'Host':"blog.csdn.net",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "X-Forwarded-For": ip,
        "User-Agent": user_agent
    }
    try:
        response = requests.request("GET", url, headers=headers,timeout=10)
    except Exception,e:
        print e
        return 0
    #print(response.text)
    return  response.text

def main():

    name = 'xunalove'
    #url = "http://blog.csdn.net/"+name+"/article/list/20"

    user_agent_list = []
    f = open('user_agent.txt','r')
    for date_line in f:
        user_agent_list.append(date_line.replace('\r\n',''))

    f.close()
    id_list = []
    f = open('id_list.txt','r')
    for date_line in f:
        id_list.append(date_line.replace('\n',''))
    f.close()

    proxy_list = []
    f = open('proxy.txt','r')
    for date_line in f:
        proxy_list.append(date_line.replace('\n',''))
    f.close()

    for i in range(100000):
        now_id = random.choice(id_list)
        now_ua = random.choice(user_agent_list)
        now_ip = random.choice(proxy_list)
        url = "http://blog.csdn.net/"+name+"/article/details/"+str(now_id)
        print i,url
        html_code = forge_headers(url,now_ua,now_ip)
        time.sleep(random.random())

    # page_id_set = set()
    # page_id = re.findall('/xunalove/article/details/[0-9]{8}',html_code)
    # for now_url in page_id:
    #     page_id_set.add(now_url[-8:])
    # #print len(page_id_set)
    # for now_set in page_id_set:
    #     print now_set


if __name__ == '__main__':

    print 'begin',time.ctime()
    main()
    print 'end',time.ctime()
