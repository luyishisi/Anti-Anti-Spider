#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：TB_Simulationo.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python TB_Simulationo.py
#   功能：淘宝模拟登陆
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 中文编码设置

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核
def main():
    driver = webdriver.Chrome()
    now_url = 'https://www.taobao.com/'
    login_url = 'https://login.taobao.com/member/login.jhtml'
    driver.get(now_url)
    name = 'temp.png'
    driver.save_screenshot(name)

    newwindow='window.open("https://www.taobao.com/");'

    driver.delete_all_cookies()
    driver.add_cookie({
     'cookie': "thw=cn; _med=dw:1280&dh:800&pw:2560&ph:1600&ist:0; cna=P2IsEanwSRwCAQHAWqiGF67j; v=0; _tb_token_=eee3b5ee33fe; uc1=cookie14=UoW%2FWvN6rMfscA%3D%3D&lng=zh_CN&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=U%2BGCWk%2F7pY%2FF&tag=7&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; uc3=sg2=BYiIfEpsMbxtm040yzQn62r4dy8462CfLR73vjezc00%3D&nk2=AimQPFamtydz&id2=UUkKfSsJrCYO&vt3=F8dARHtAw8YORZlfWNE%3D&lg2=UIHiLt3xD8xYTw%3D%3D; hng=CN%7Czh-cn%7CCNY; existShop=MTQ4NzIzODY0Mw%3D%3D; uss=UUo3ufYf5xKnNsaX1Did8zEif4JWaXQKBqHBcNPFsBnDoRjsJJLEk3H3; lgc=a83533774; tracknick=a83533774; cookie2=1ce7c2d2ca6f9c4ae2d6572991049a5c; sg=450; mt=np=; cookie1=VFRzDaFMVd2CkhbafcMIU%2FP3OBRn%2FPsNhKwkjUH18W0%3D; unb=214163505; skt=c6537c77a7d1eeab; t=7770838b844b0e51e306c6d6ea1afd1d; publishItemObj=Ng%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=a83533774; cookie17=UUkKfSsJrCYO; l=AiIincM6w0qeIuxe-pmmoAbh8qKF/yZm; isg=AiAgn3SvbMYgs9DCPrh-kuXo8Sh8CgTzgPI-RZowYDsllcK_QjisgmnlW4rv"
    })

    driver.execute_script(newwindow)
    input("查看效果")

    #time.sleep(20)
    driver.quit()
    driver.close()


# driver = webdriver.PhantomJS()
# print 'begin',time.ctime()
# dcap = dict(DesiredCapabilities.PHANTOMJS)
#
# dcap["phantomjs.page.settings.userAgent"]=(
# "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
# )
#
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
#发起请求≈
#
# js1 = 'return document.body.scrollHeight'
# #js2 = 'window.scrollTo(0, document.body.scrollHeight)'
# old_scroll_height = 0
# num = 300
# max_num = driver.execute_script(js1)
# add_num = max_num / 20
# while(max_num > num ):
#     num += add_num
#     js2 = 'window.scrollTo(0, '+str(num)+')'
#     driver.execute_script(js2)
#     time.sleep(0.2)
#     max_num = driver.execute_script(js1)
#     #add_num = max_num / 20
#     print num,'/',max_num
# time.sleep(4)#主要等待时间延迟可设置
#
# name = str(id)+'.png'
# driver.save_screenshot(name)
# print name
#
# #获取用户名框并输入
# # elem = driver.find_element_by_xpath('//*[@id="email"]')
# # elem.send_keys("****")
#
# #获取密码框并输入
# # elem = driver.find_element_by_xpath('//*[@id="password"]')
# # elem.send_keys("****")
#
# #通过回车键进行登录
# #elem.send_keys(Keys.RETURN)
#
# # 通过id选择到登录键
# # driver.find_element_by_id('submit-button').click()
#
#
# # time.sleep(2)
#
# #保存页面截图和源码
# #name = '~/so_img/'+time.ctime().replace(' ','-')+'.png'
# # name = time.ctime().replace(' ','-')+'.png'
# #name_html = "~/so_img/"+time.ctime().replace(' ','-')+'.html'
#
# # driver.save_screenshot(name)
# #f = open(name_html.encode('utf-8'),'w')
# #f.write(driver.page_source)
# #f.close()
#
# #print driver.page_source
#
# # time.sleep(5)
#
# # print 'end',time.ctime()
# #elem.clear()
# #time.sleep(10)



if __name__ == '__main__':
    main()
