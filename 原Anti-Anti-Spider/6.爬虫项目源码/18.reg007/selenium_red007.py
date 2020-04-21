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

def get_chrome():
    # 加载内核
    driver = webdriver.Chrome()
    # 发起请求
    print ('beging_0')
    url ='https://www.reg007.com/account/signin'
    driver.get(url)

    # 获取用户名框并输入密码完成登录操作
    elem = driver.find_element_by_xpath('//*[@id="signin_email"]').send_keys("zhanghao@qq.com")
    elem = driver.find_element_by_xpath('//*[@id="signin_password"]').send_keys("mima")
    elem = driver.find_element_by_xpath('//*[@id="signin_form"]/button').click()
    time.sleep(1)
    # 跳转到搜索页面
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ol/li[1]/a').click()

    elem = driver.find_element_by_xpath('//*[@id="e_m"]')
    elem.send_keys("18322867654")
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="tsb"]').click()

    time.sleep(10)
    with open("code.html","wb") as f:
        f.write(driver.page_source.encode('utf8'))
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    get_chrome()
