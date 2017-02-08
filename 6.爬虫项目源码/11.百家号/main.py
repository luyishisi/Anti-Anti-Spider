#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------
#   程序：baijiahao.py
#   版本：1
#   作者：ly
#   日期：编写日期2017/1/20
#   语言：Python 2.7.x
#   操作：python GDToOSM.py Table
#   功能：从内部接口爬去百家号url
#------------------------------------------------------------------------------------------

import requests
import json,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()
url = "http://baijiahao.baidu.com/api/content/article/listall?sk=super&ak=super&\
    app_id=1541190710072607&_skip=0&_limit=295&status=in:publish,published&\
    _preload_statistic=1&_timg_cover=50,172,1000&_cache=1"

url = "https://club.jd.com/comment/productPageComments.action?callback=\
fetchJSON_comment98vv31400&productId=3133813&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0"

body = requests.get(url).text.encode('utf8').decode('utf8')

print body[26:]
time.sleep(10)

body_json = type(eval(body[26:]))

print body_json
#for i in range(len(body_json['items'])):
    #print body_json['items'][i]['id']
