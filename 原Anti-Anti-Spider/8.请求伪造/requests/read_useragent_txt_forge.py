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


#此处修改头字段,


#发起请求,
def get_request(url,user_agent):
	'''参数引入及头信息'''
	if len(user_agent ) < 10:
		user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'

	headers = {
    	'Host':"map.baidu.com",
    	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    	"Accept-Encoding": "gzip, deflate",
    	"Accept-Language": "en-US,en;q=0.5",
    	"Connection": "keep-alive",
    	"User-Agent": user_agent
	}

	#可设置代理
    #proxies = {
	#	"http": "http://"+ip,
	#	"https": "http://"+ip,
	#}
    #url = "https://www.urlteam.org"

	html=requests.get(url,headers=headers, timeout=10).text
	print html
	return html

if __name__ == '__main__':
	url = "https://shop.m.taobao.com/shop/coupon.htm?sellerId=102077180&activityId=c81d798cbbc143c8b443d2b73b81b2bf&qq-pf-to=pcqq.group"

	#导入数据集
	user_agent_list = []
	f = open('user_agent.txt','r')
	for date_line in f:
		user_agent_list.append(date_line.replace('\r\n',''))

	k = 1
	for i in range(k):
		print i,random.choice(user_agent_list)
		user_agent = random.choice(user_agent_list)

		get_request(url,user_agent)
