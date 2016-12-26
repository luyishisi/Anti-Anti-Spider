#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：shimu.py
#   版本：0.1
#   作者：copie
#   日期：编写日期2016/12/15
#   语言：Python 3.5.x
#   系统:   archlinux 
#   操作：python shimu.py
#   功能：
#-------------------------------------------------------------------------
from selenium import webdriver
import time

browser = webdriver.PhantomJS()
browser.get('http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html')
time.sleep(10)
browser.get('http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html')
files = open('ziliao.txt','w')
body=browser.find_element_by_xpath('//*[@id="managerList"]/tbody')
nextButton=browser.find_element_by_xpath('//*[@id="managerList_paginate"]/a[3]')
t=browser.find_element_by_xpath('//*[@id="managerList_length"]/label/select/option[4]')
t.click()
i=1
while 1:
    str=body.text
    strs=str.split('\n')
    for s in strs:
        files.writelines(s)
        files.writelines('\n')
    print(len(strs))
    if  len(strs) < 100:
        break
    nextButton.click()
    print(i)
    i=i+1
    time.sleep(5)
files.close()
browser.close()

