#coding:utf-8
import requests


#此处修改头字段,
headers = {
    'Host':"map.baidu.com",
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

	html=requests.get(url,headers=headers, timeout=10).text
	print html
	return html

if __name__ == '__main__':
	url = "https://www.urlteam.org"
	get_request(url,headers)
	
