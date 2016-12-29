#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：发出请求并且解析
#
#-------------------------------------------------------------------------
import requests
import time,sys,json

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

url = 'https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E7%9A%AE%E8%A3%A4%E7%94%B7&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=1'
body = requests.get(url)
body = body.text.encode('utf8')

dic_body = eval(body)
print type(dic_body)
print dic_body["RN"]
print dic_body["listItem"][0]
