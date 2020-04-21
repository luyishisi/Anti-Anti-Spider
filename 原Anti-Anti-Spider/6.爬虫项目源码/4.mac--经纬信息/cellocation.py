#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：cellocation.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python cellocation.py
#   功能：目标网站http://api.cellocation.com/rewifi.html  需求的数据为该经纬度信息和附近的mac地址的对应信息.
#         采集方式是伪造请求头,从该网站的内部接口找到他.
#
#-------------------------------------------------------------------------
import requests


#此处修改头字段,
headers = {
#    'Host':"map.baidu.com",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Encoding": "gzip, deflate",
#    "Accept-Language": "en-US,en;q=0.5",
#    "Connection": "keep-alive",
#    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0",
#    "referer" : '123.123.123.123'#
#GET /rewifi.html?incoord=gcj02&coord=gcj02&lat=39.964556&lon=116.302214 HTTP/1.1
"Host": "api.cellocation.com",
"Connection": "keep-alive",
"Pragma": "no-cache",
"Cache-Control": "no-cache",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8"
}


#发起请求,
def get_request(url,headers):
	'''参数引入及头信息'''
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
	url = "http://api.cellocation.com/rewifi/?incoord=gcj02&coord=gcj02&lat=39.98373&lon=116.322428"
	get_request(url,headers)
	print headers
