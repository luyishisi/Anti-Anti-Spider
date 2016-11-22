#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：read_useragent_txt_forge.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python read_useragent_txt_forge.py
#   功能：	读取一个随机的头部User-Agent 信息 添加到请求中
#
#-------------------------------------------------------------------------
import requests
import random
import time


#此处修改头字段,


#发起请求,
def get_request(url,now_user_agent,ip,post):
    '''参数引入及头信息'''
   # global use_headers
    if len(user_agent ) < 10:
        now_user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
    use_headers = {
        'Host':"ip.rtbasia.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate,sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        #"Connection": "keep-alive",
        "User-Agent": now_user_agent,
        'Referer':'https://ip.rtbasia.com/map/ip?ip=171.8.132.64'
    }
    
    print use_headers
    print ip,post

    #url = "https://www.urlteam.org"
    url = 'https://ip.rtbasia.com/map/ip?ip=171.8.132.64'
    proxies = { 
        "http": "http://"+ip+':'+post,
        "https": "https://"+ip+':'+post,
    }
    print '*'*100
    print proxies
    print requests.get('http://icanhazip.com/',proxies=proxies).text
    time.sleep(1)
    print '*'*100
    #html=requests.get(url,headers=use_headers, timeout=20).text
    html=requests.get(url,headers = use_headers, proxies=proxies,timeout=30).text
    #html=requests.get(url, timeout=10).text
    print html
    return html

if __name__ == '__main__':
    url = "https://www.urlteam.org"
    #导入数据集
    user_agent_list = []
    f = open('user_agent.txt','r')
    for date_line in f:
        user_agent_list.append(date_line.replace('\r\n',''))
    f.close()
    k = 1

    ip = '120.37.172.81'
    post = '808'



    for i in range(k):
        print i,random.choice(user_agent_list)
        user_agent = random.choice(user_agent_list)
        get_request(url,user_agent,ip,post)



