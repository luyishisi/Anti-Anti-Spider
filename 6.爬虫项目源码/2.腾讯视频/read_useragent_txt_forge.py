#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：read_useragent_txt_forge.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/25
#   语言：Python 2.7.x
#   操作：python read_useragent_txt_forge.py
#   功能：	爬取腾讯视频播放链接
#         读取一个随机的头部User-Agent 信息 添加到请求中此作为基础的伪造,
#
#-------------------------------------------------------------------------
import requests
import random
import re
import os

#发起请求,
def get_request(url):
	try:
		# 字符串连接成命令,注意保留空格
		common = 'phantomjs ' + 'forge_X_FORWARDED_FOR.js '+ url
		print common
		str_body =  str(os.popen(common).read())
		#html=requests.get(url,headers=headers, timeout=20).text
		print str_body
		return str_body
	except Exception,e:
		print Exception,e
		return -1

if __name__ == '__main__':
	#此url为任意一个具有某视频播放窗口的页面
	url = "https://v.qq.com/x/cover/u3cgw9e383hnl7z/n0022y6dfv7.html"

	#发起请求
	html_body = get_request(url)

	print re.findall('https://imgcache.qq.com/tencentvideo_v1/.*=0',html_body)


#-------------------测试结果-------------------------------
# 将此链接放在浏览器中可以直接播放,虽然有广告....至于别的数据太简单那就不抓了.

[
'https://imgcache.qq.com/tencentvideo_v1/playerv3/TPout.swf?max_age=86400&amp;v=20161117&amp;vid=n0022y6dfv7&amp;auto=0',
'https://imgcache.qq.com/tencentvideo_v1/playerv3/TPout.swf?max_age=86400&amp;v=20161117&amp;vid=n0022y6dfv7&amp;auto=0'
]
