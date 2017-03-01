#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：结合crontab定时启动每天自动登录so网站,刷银牌用
#-------------------------------------------------------------------------

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

# 加载内核
driver = webdriver.PhantomJS()

# 发起请求≈
for i in range(10, 20):
    try:
        print i, 'begin', time.ctime()
        num = i
        url = 'http://as-rank.caida.org/?mode0=as-info&mode1=as-table&as=' + \
            str(num) + '&data-selected-id=39'
        driver.implicitly_wait(10)
        driver.get(url)
        # 保存页面截图和源码
        name = './png/' + str(num) + '.png'
        name_html = "./code/" + str(num) + '.html'

        driver.save_screenshot(name)
        f = open(name_html, 'w')
        f.write(driver.page_source)
        f.close()

        # time.sleep(5)
        print i, 'end  ', time.ctime()
    except Exception, e:
        print e
driver.close()
