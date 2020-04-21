#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：taobao_login.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能： 淘宝页面登录
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核

def main():
    print 'begin',time.ctime()
    driver = webdriver.Chrome()
    url = 'http://jiaowu.pdsu.edu.cn/'
    driver.get(url)
    time.sleep(1)
    #driver.find_element_by_id('m14').click()#点击进入密码区域
    # time.sleep(1)txt_asmcdefsddsd

    now_handle = driver.current_window_handle #得到当前窗口句柄
    #driver.find_element_by_id("baidu").click()
    all_handles = driver.window_handles #获取所有窗口句柄
    print now_handle,all_handles
    time.sleep(1)
    # handle = all_handles[0]
    # driver.switch_to_window(handle)
    # now_handle = driver.current_window_handle
    # print now_handle
    time.sleep(1)

    driver.find_element_by_id('m14').click()#点击进入密码区域

    driver.switch_to_frame('frmHomeShow')

    elem = driver.find_element_by_xpath('//*[@id="txt_asmcdefsddsd"]')
    time.sleep(1)
    elem.send_keys("131360104")
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="txt_pewerwedsdfsdff"]')
    elem.send_keys("1")#x  frmHomeShow

    elem = driver.find_element_by_xpath('//*[@class="tx1"]')
    elem.click()
    #driver.find_element_by_id('txt_sdertfgsadscxcadsads').click()

    # elem = driver.find_element_by_xpath('//*[@id="TPL_password_1"]')
    # elem.send_keys("l")
    # try:
    #     begin = driver.find_element_by_xpath('//span[@class="nc_iconfont btn_slide"]')
    #     time.sleep(1)
    #     print '1'
    #     end = driver.find_element_by_xpath('//i[@id="J_Static2Quick"]')
    #     time.sleep(1)
    #     print '2'
    #     ActionChains(driver).drag_and_drop(begin,end).perform()
    #     time.sleep(1)
    #     print '3'
    #     driver.find_element_by_id('J_SubmitStatic').click()
    #     print '4'
    # except:
    #     print '0'
    #     driver.find_element_by_id('J_SubmitStatic').click()
    # #being.click()
    # # driver.find_element_by_id('J_Quick2Static').click()#点击进入密码区域
    #time.sleep(1)

    #time.sleep(1)
    name = 'temp1.png'
    driver.save_screenshot(name)

    #处理滑块拖动问题
    #id= nc_1_n1z
    #ActionChains

    time.sleep(10)
    # name = 'temp1.png'
    # driver.save_screenshot(name)
    print 'end',time.ctime()
    driver.quit()
    #driver.close()


if __name__ == '__main__':
    main()


#driver = webdriver.Chrome()
# dcap = dict(DesiredCapabilities.PHANTOMJS)

# dcap["phantomjs.page.settings.userAgent"]=(
# "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
# )

#driver = webdriver.PhantomJS(desired_capabilities=dcap)
#发起请求≈
# for i in range(20):
#     #id = 31780000-i
#     id = 3000029+i
#     now_url = 'http://invest.ppdai.com/loan/info?id='+str(id)
#     driver.get(now_url)
#
#     js1 = 'return document.body.scrollHeight'
#     #js2 = 'window.scrollTo(0, document.body.scrollHeight)'
#     old_scroll_height = 0
#     num = 300
#     max_num = driver.execute_script(js1)
#     add_num = max_num / 20
#     while(max_num > num ):
#         num += add_num
#         js2 = 'window.scrollTo(0, '+str(num)+')'
#         driver.execute_script(js2)
#         time.sleep(0.2)
#         max_num = driver.execute_script(js1)
#         #add_num = max_num / 20
#         print num,'/',max_num
#     time.sleep(4)#主要等待时间延迟可设置
#
#     name = str(id)+'.png'
#     driver.save_screenshot(name)
#     print name

#获取用户名框并输入
# elem = driver.find_element_by_xpath('//*[@id="email"]')
# elem.send_keys("****")

#获取密码框并输入
# elem = driver.find_element_by_xpath('//*[@id="password"]')
# elem.send_keys("****")

#通过回车键进行登录
#elem.send_keys(Keys.RETURN)

# 通过id选择到登录键
# driver.find_element_by_id('submit-button').click()


# time.sleep(2)

#保存页面截图和源码
#name = '~/so_img/'+time.ctime().replace(' ','-')+'.png'
# name = time.ctime().replace(' ','-')+'.png'
#name_html = "~/so_img/"+time.ctime().replace(' ','-')+'.html'

# driver.save_screenshot(name)
#f = open(name_html.encode('utf-8'),'w')
#f.write(driver.page_source)
#f.close()

#print driver.page_source

# time.sleep(5)

# print 'end',time.ctime()
#driver.quit()
#elem.clear()
#time.sleep(10)
#driver.close()
