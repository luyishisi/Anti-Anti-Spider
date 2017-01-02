#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/12/31
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys
from lxml import etree#
import re

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核
driver = webdriver.PhantomJS()
#发起请求
print 'beging_0'
#url ="https://item.taobao.com/item.htm?id=538287375253&abtest=10&rn=07abc745561bdfad6f726eb186dd990e&sid=46f938ba6d759f6e420440bf98b6caea"
url ='https://detail.m.tmall.com/item.htm?id=535592571726&abtest=10&rn=07abc745561bdfad6f726eb186dd990e&sid=46f938ba6d759f6e420440bf98b6caea'
driver.get(url)


elem = driver.find_element_by_xpath('//a[@class="desc"]').click()
time.sleep(3)

print '3'
html = driver.page_source.encode('utf-8')

print html
# selector=etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))
# context=selector.xpath('//ul[@class="attributes-list"]/li')
# list_date = u''
# for i in range(len(context)):
#     a = etree.tostring(context[i], encoding="utf-8")#.encode('utf-8')
#     b = a.split('>')
#     end  = b[1].split('<')[0]+';'
#     list_date += end
#
# print list_date.encode('utf8')
print 'end'
driver.quit()
