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
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
# 发起请求
print 'beging_0'
# driver.get("http://lbsyun.baidu.com/skins/MySkin/resources/iframs/heightAccApi.html")
# driver.get("https://s.m.taobao.com/h5?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&sst=1&n=20&buying=buyitnow&q=%E7%9A%AE%E8%A3%A4%E5%A5%B3")
driver.get("https://h5.m.taobao.com/awp/core/detail.htm?id=538287375253&abtest=25&rn=51380cce73c6e338c4f512e1d592ddb7&sid=a706d7e5bb79cfe64053bad190a02f4c")
# http://lbsyun.baidu.com/index.php?title=webapi/high-acc-ip

# 获取用户名框并输入
print 'beging_1'
#elem = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/input')

# elem.send_keys("171.15.132.58")

# 获取密码框并输入
# print 'beging_2'
elem = driver.find_element_by_xpath(
    '//*[@class="desc_page_box normal"]').click()
# elem.send_keys("**")desc_page_box normal
# 通过回车键进行登录
# print 'beging_3'
# elem.send_keys(Keys.RETURN)

# time.sleep(10)
js1 = 'return document.body.scrollHeight'
js2 = 'window.scrollTo(0, document.body.scrollHeight)'

old_scroll_height = 0
while(driver.execute_script(js1) > old_scroll_height):
    old_scroll_height = driver.execute_script(js1)
    driver.execute_script(js2)
    time.sleep(3)
    name = '' + time.ctime().replace(' ', '-') + '.png'
    driver.save_screenshot(name)
# 保存页面截图和源码
name = '' + time.ctime().replace(' ', '-') + '.png'
driver.save_screenshot(name)
#f = open(name_html.encode('utf-8'),'w')
# f.write(driver.page_source)
# f.close()

# print driver.page_source.encode('utf8')

time.sleep(5)

# driver.quit()
# elem.clear()
# time.sleep(10)
driver.close()
