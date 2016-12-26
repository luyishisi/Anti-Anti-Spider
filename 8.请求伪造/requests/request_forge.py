#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：referer_forge.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python request_forge.py
#   功能：	简单的样例代码
#
#-------------------------------------------------------------------------
import requests
import re,sys
from lxml import etree

# --------------------------------------------------
# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()


#此处修改头字段,
headers = {
    'Host':"www.xicidaili.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
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

	html=requests.get(url,headers=headers, timeout=10).text#.decode('utf-8')
	print html
	return html

if __name__ == '__main__':
    url = "http://www.xicidaili.com/nn"
    html_code = get_request(url,headers)

    re_list_ip = re.findall(r'<td>\d*\.\d*\.\d*\.\d*</td>',html_code)
    re_list_port = re.findall(r'<td>[\d]*</td>',html_code)
    re_list_live_time = re.findall(r'<td>\d*[小时分钟天]*</td>',html_code)
    re_list_time = re.findall(r'<td>\d*-\d*-\d* \d*:\d*</td>',html_code)
    l = len(re_list_ip)
    print len(re_list_port)
    print len(re_list_live_time)
    print len(re_list_time)


    #for i in range(l):
