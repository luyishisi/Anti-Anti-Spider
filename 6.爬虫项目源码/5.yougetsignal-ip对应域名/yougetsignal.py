#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：yougersignal.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python yougersignal.py
#   功能：目标网站 http://www.yougetsignal.com/tools/web-sites-on-web-server/
#         需求的信息是点击check后将增加的url和ip信息
#         从js中分析,该网站是用,ajax后期加载,并且是用post的方式讲字符串连接到url后面的.
#         所以不可以使用from表单的形式发送请求,而是要用直接讲表单写成字符串里
#
#-------------------------------------------------------------------------

import requests

url = "http://domains.yougetsignal.com/domains.php"

payload = "remoteAddress=www.baidu.com"

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

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
