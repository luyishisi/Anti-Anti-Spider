#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：拍拍贷页面截图
#-------------------------------------------------------------------------

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

# 加载内核

#driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
print 'begin', time.ctime()
dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)

driver = webdriver.PhantomJS(desired_capabilities=dcap)
# 发起请求≈
for i in range(20):
    #id = 31780000-i
    id = 3000029 + i
    now_url = 'http://invest.ppdai.com/loan/info?id=' + str(id)
    driver.get(now_url)

    js1 = 'return document.body.scrollHeight'
    #js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    old_scroll_height = 0
    num = 300
    max_num = driver.execute_script(js1)
    add_num = max_num / 20
    while(max_num > num):
        num += add_num
        js2 = 'window.scrollTo(0, ' + str(num) + ')'
        driver.execute_script(js2)
        time.sleep(0.2)
        max_num = driver.execute_script(js1)
        #add_num = max_num / 20
        print num, '/', max_num
    time.sleep(4)  # 主要等待时间延迟可设置

    name = str(id) + '.png'
    driver.save_screenshot(name)
    print name

# 获取用户名框并输入
# elem = driver.find_element_by_xpath('//*[@id="email"]')
# elem.send_keys("****")

# 获取密码框并输入
# elem = driver.find_element_by_xpath('//*[@id="password"]')
# elem.send_keys("****")

# 通过回车键进行登录
# elem.send_keys(Keys.RETURN)

# 通过id选择到登录键
# driver.find_element_by_id('submit-button').click()


# time.sleep(2)

# 保存页面截图和源码
#name = '~/so_img/'+time.ctime().replace(' ','-')+'.png'
# name = time.ctime().replace(' ','-')+'.png'
#name_html = "~/so_img/"+time.ctime().replace(' ','-')+'.html'

# driver.save_screenshot(name)
#f = open(name_html.encode('utf-8'),'w')
# f.write(driver.page_source)
# f.close()

# print driver.page_source

# time.sleep(5)

# print 'end',time.ctime()
driver.quit()
# elem.clear()
# time.sleep(10)
driver.close()
