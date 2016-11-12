#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：Focus_Spider.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python Focus_Spider.py
#   功能：测试聚焦爬虫,自动抓取urlteam网站的全部url.可以通过修改正则来调整匹配到url
#		 通过.修改main中的导入url来设置入口网站.搜索方式是随机,随着数值的增加匹配深度
#
#-------------------------------------------------------------------------
import re, requests, sys, random

#--------------------------------------------------
#中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

set_url = set() # 防止重复
def requests_url(url):
	try:
		page_html = requests.get(url).text.encode('utf-8')
		#print page_html
		#url_list = re.findall('http://.*\'',page_html)
		url_list = re.findall('''https?://.{4}urlteam[^"<>()\s']+''',page_html)
		for i in url_list:
			if( i.find('.jpg')==-1 and i.find('.png')==-1 and i.find('/js/')==-1 and i.find('.css?')==-1 and i.find('.js')==-1 ):
				#print i
				set_url.update([i])
		return set_url

		#print url_list

	except Exception,e:
		print Exception,e

if __name__=='__main__':
	#入口
	url = 'https://www.urlteam.org'

	requests_url(url)
	#print set_url
	#print len(set_url)
	num = 400  #设置随机次数.随意设置用于测试

	while(num):
		l = len(set_url)
		n = random.randint(0,l)
		temp_flag = 0
		for temp_url in set_url:
			temp_flag += 1
			if temp_flag == n:
				break
			url = temp_url
		print num,temp_url,url

		try:
			requests_url(url)
		except Exception,e:
			print Exception,e

		print len(set_url)
		num -= 1


#--------------------------------------------------
#写入文件.
	print set_url
	print len(set_url)
	f = open('set.txt','w')
	f.write(str(set_url))
	f.write(str(len(set_url)))
	f.close()
