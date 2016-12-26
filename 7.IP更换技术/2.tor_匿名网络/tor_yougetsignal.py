#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：yougersignal.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python yougersignal.py
#   环境：linux ubuntu 16.04 已经翻墙
#   功能：目标网站 http://www.yougetsignal.com/tools/web-sites-on-web-server/
#         使用tor更换代理ip
#         需求的信息是点击check后将增加的url和ip信息
#         从js中分析,该网站是用,ajax后期加载,并且是用post的方式讲字符串连接到url后面的.
#         所以不可以使用from表单的形式发送请求,而是要用直接讲表单写成字符串里
#
#-------------------------------------------------------------------------

import requests
import os
import requesocks
import time



headers = {
    'host': "domains.yougetsignal.com",
    'connection': "keep-alive",
    'content-length': "35",
    'pragma': "no-cache",
    'cache-control': "no-cache",
    'origin': "http://www.yougetsignal.com",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "text/javascript, text/html, application/xml, text/xml, */*",
    'x-prototype-version': "1.6.0",
    'x-requested-with': "XMLHttpRequest",
    'referer': "http://www.yougetsignal.com/tools/web-sites-on-web-server/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'postman-token': "87da47a1-61bd-04e3-f765-134f97a469c1"
}


def getip_requests(url):
    try:
        print "(+) Sending request with plain requests..."
        r = requests.get(url)
        print "(+) my_IP is: " + r.text.replace("\n", "")
        return r.text.replace("\n", "")
    except Exception,e:
        print Exception,e
        return -1

def getip_requesocks(url):
    try:
        print "(+) Sending request with requesocks..."
        session = requesocks.session()
        session.proxies = {'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'}
        r = session.get(url,timeout = 30)
        print "(+) tor_IP is: " + r.text.replace("\n", "")
        return  r.text.replace("\n", "")
    except Exception,e:
        print Exception,e
        return -1

def Ip_checksum(num):
    """检查本机与tor后的ip地址,参数为重试次数,成功返回1"""
    while(num):
        num -= 1
        my_url = 'http://api.ipify.org?format=json'
        print "检查本机与tor后的ip地址tests..."
        my_ip = getip_requests(my_url)
        tor_ip = getip_requesocks(my_url)
        if(my_ip == tor_ip or my_ip == -1 or tor_ip == -1):
            os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo \
            quit) | nc localhost 9051""")
            time.sleep(3)
        if(my_ip != tor_ip and my_ip != -1 and tor_ip != -1):
            print "tor连接成功,当前ip为:",tor_ip
            return 1
    print "tor链接失败,请检查网络"
    return 0

def get_data(ip,url,headers):
    #payload = "remoteAddress="+str(ip)
    payload = "remoteAddress=digg.com&key=&_="

    #session = requesocks.session()
    #session.proxies = {'http': 'socks5://127.0.0.1:9050',
    #'https': 'socks5://127.0.0.1:9050'}
    #payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"remoteAddress\"\r\n\r\nwww.baidu.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"key\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    #r = session.post(url,timeout=30,data=payload,headers=headers)
    proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
    }
    print '*'*100
    #print r.text
    response = requests.request("POST", url, data=payload,proxies= proxies ,headers=headers)
    print '*'*100
    #response = requests.request("POST", url, data=payload)
    print(response.text)

def main():
    global headers
    Ip_checksum(3)
    url = "http://domains.yougetsignal.com/domains.php"
    #url = "https://movie.douban.com/j/search_subjects"
    ip = '120.27.101.31'
    get_data(ip,url,headers)





if __name__ == "__main__":
    main()
