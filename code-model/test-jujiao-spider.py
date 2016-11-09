#coding:utf-8
import re
import requests
import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

set_url = set()
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
	#set set_url 
	url = 'https://www.urlteam.org'
	requests_url(url)
	#print set_url
	print len(set_url)
	num = 400
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
	print set_url
	print len(set_url)
	f = open('set.txt','w')
	f.write(str(set_url))
	f.write(str(len(set_url)))
	f.close()
	


	
		
	

