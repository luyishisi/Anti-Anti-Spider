# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome()

url = "https://www.baidu.com/"
browser.get(url)
# 通过js新打开一个窗口
newwindow='window.open("https://www.baidu.com");'
# 删除原来的cookie
browser.delete_all_cookies()
# 携带cookie打开
browser.add_cookie({'name':'ABC','value':'daye'})
# 通过js新打开一个窗口
browser.execute_script(newwindow)
input("查看效果")
browser.quit()
