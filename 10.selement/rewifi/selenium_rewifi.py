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
driver = webdriver.Chrome()

#发起请求
driver.get("http://api.cellocation.com/rewifi.html")

#获取用户名框并输入
elem = driver.find_element_by_xpath('//*[@id="lat"]')
#elem.send_keys("39.96593")

#获取密码框并输入
elem = driver.find_element_by_xpath('//*[@id="lon"]')
#elem.send_keys("116.304616")

#通过回车键进行登录
#elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_xpath('/html/body/div[1]/input[3]').click()
time.sleep(5)

#保存页面截图和源码
#name = '~/so_img/'+time.ctime().replace(' ','-')+'.png'
name = time.ctime().replace(' ','-')+'.png'
#name_html = "~/so_img/"+time.ctime().replace(' ','-')+'.html'

driver.save_screenshot(name)
#f = open(name_html.encode('utf-8'),'w')
#f.write(driver.page_source)
#f.close()

print driver.page_source

time.sleep(5)

print 'end',time.ctime()
#driver.quit()
#elem.clear()
#time.sleep(10)
driver.close()
