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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核
driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
#发起请求
print 'beging_0'

driver.get("https://www.adidas.com.cn/")
#driver.get("https://www.adidas.com.cn/customer/account/login/")

print 'beging_1'
#获取密码框并输入
time.sleep(5)
name = ''+time.ctime().replace(' ','-')+'.png'

print 'beging_3'
try:
    elem = driver.find_element_by_id('email')#.click()
    elem.send_keys('luyishisi')
except Exception,e:
    print e
try:
    elem = driver.find_element_by_id('pass')#.click()
    elem.send_keys('luyi123')
except Exception,e:
    print e

time.sleep(2)
name = ''+time.ctime().replace(' ','-')+'.png'
driver.save_screenshot(name)
elem.send_keys(Keys.RETURN)
    #J_autocomplete
print 'beging_3'
#获取密码框并输入
#print 'beging_2'
#elem = driver.find_element_by_xpath('//*[@class="desc_page_box normal"]').click()
#elem = driver.find_element_by_xpath('//*[@data-reactid=".0.1.0.0.1"]').click()
#elem = driver.find_element_by_xpath('//*[@data-reactid=".0.1.0.0.0"]').click()

#.0.1.0.0.0
#elem.send_keys("**")desc_page_box normal

#通过回车键进行登录
#print 'beging_3'
#elem.send_keys(Keys.RETURN)

#time.sleep(10)
# js1 = 'return document.body.scrollHeight'
# js2 = 'window.scrollTo(0, document.body.scrollHeight)'

# old_scroll_height = 0
# while(driver.execute_script(js1) > old_scroll_height):
#     old_scroll_height = driver.execute_script(js1)
#     driver.execute_script(js2)
#     time.sleep(3)
#     name = ''+time.ctime().replace(' ','-')+'.png'
#     driver.save_screenshot(name)
#保存页面截图和源码
#print driver.page_source.encode('utf-8')
time.sleep(5)
name = ''+time.ctime().replace(' ','-')+'.png'
driver.save_screenshot(name)

#f = open(name_html.encode('utf-8'),'w')
#f.write(driver.page_source)
#f.close()

#print driver.page_source.encode('utf8')

print 'end'
driver.quit()
#elem.clear()
#time.sleep(10)
driver.close()
