#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   name: read_list.py
#   版本：1
#   作者：ly
#   日期：编写日期2016/12/31
#   语言：Python 2.7.x
#   操作：python read_list.py
#   功能：读取文件列表，将淘宝商品信息截图存放
#        文件的格式要求为一行一个商品url
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)


# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#加载内核
#driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
driver = webdriver.PhantomJS(desired_capabilities=dcap)

#发起请求

import fileinput

def image_joint(image_list,opt,end_name):#opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num=len(image_list)
    image_size=image_list[0].size
    height=image_size[1]
    width=image_size[0]
    if opt=='vertical':
        new_img=Image.new('RGB',(width,image_num*height),255)
    else:
        new_img=Image.new('RGB',(image_num*width,height),255)
    x=y=0
    count=0
    for img in image_list:
        new_img.paste(img,(x,y))
        count+=1
        if opt=='horizontal':
            x+=width
        else : y+=height

    new_img.show()
    new_img.save(end_name)
    #return new_img


list_url = []
i  = 0
for line in fileinput.input("list.txt"):
    #print line
    url = line.replace('\n','').replace('\r','')
    print '请求发起中，请等待'
    #driver.get("https://h5.m.taobao.com/awp/core/detail.htm?id=538287375253&abtest=25&rn=51380cce73c6e338c4f512e1d592ddb7&sid=a706d7e5bb79cfe64053bad190a02f4c")
    driver.get(url)
    time.sleep(3)

    if(url.find('taobao') != -1):
        #可找到taobao则 返回值不为-1
        print driver.title.encode('utf-8')
        try:
            #需求修改，无需进行淘宝详情页面的截图采集
            #print '页面加载完成，进行截图保存'
            #print '触发淘宝页面商品参数页面点击事件'
            #elem = driver.find_element_by_xpath('//*[@data-reactid=".0.1.0.0.1"]').click()
            #print '事件完成'
            #name = ''+time.ctime().replace(' ','-')+'.png'
            #driver.save_screenshot(name)
            pass
        except Exception,e:
            print e
        try:
            print '加载中'
            elem = driver.find_element_by_xpath('//*[@data-reactid=".0.1.0.0.0"]').click()

            # 后期加载需要模拟滑轮进行控制
            js1 = 'return document.body.scrollHeight'
            #js2 = 'window.scrollTo(0, document.body.scrollHeight)'
            old_scroll_height = 0
            num = 300
            max_num = driver.execute_script(js1)
            add_num = max_num / 10
            while(max_num > num ):
                num +=  add_num
                js2 = 'window.scrollTo(0, '+str(num)+')'
                driver.execute_script(js2)
                time.sleep(2)
                print num,'/',max_num
            time.sleep(5)
            #name = ''+time.ctime().replace(' ','-')+'.png'
            #driver.save_screenshot(name)
            #time.sleep(15)
            print '事件完成,进行截图保存'
            name = ''+time.ctime().replace(' ','-')+'.png'
            driver.save_screenshot(name)
        except Exception,e:
            print e

    if(url.find('tmall') != -1):
        #可找到tmall则 返回值不为-1
        try:
            print '检测为天猫页面，进行商品页面截图'
            print driver.title.encode('utf8')
            name = ''+time.ctime().replace(' ','-')+'.png'
            driver.save_screenshot(name)
            img_name_1 = name
            # try:
            #     print "检测是否有弹窗"
            #     #print '触发天猫页面点击事件'
            #     elem = driver.find_element_by_xpath('//i[@class="btn-close"]').click()
            #     #name = ''+time.ctime().replace(' ','-')+'.png'
            #     #driver.save_screenshot(name)
            #     print '弹窗结束'
            # except Exception,e:
            #     pass
                #print e
            try:
                elem = driver.find_element_by_xpath('//a[@class="desc"]').click()
                time.sleep(3)

                # 后期加载需要模拟滑轮进行控制
                js1 = 'return document.body.scrollHeight'
                #js2 = 'window.scrollTo(0, document.body.scrollHeight)'
                old_scroll_height = 0
                num = 300
                max_num = driver.execute_script(js1)
                add_num = max_num / 10

                while(max_num > num):
                    num += add_num
                    js2 = 'window.scrollTo(0, '+str(num)+')'
                    driver.execute_script(js2)
                    time.sleep(2)
                    print num,'/',max_num
                time.sleep(5)
                name = ''+time.ctime().replace(' ','-')+'.png'
                driver.save_screenshot(name)
                img_name_2 = name

                print '事件完成'
            except Exception,e:
                print
        except Exception,e:
            print e
        try:
            print "图片合成"
            print img_name_1
            print img_name_2
            opt = 'vertical'
            image_list = [img,img1]
            end_name = ''
            image_joint(image_list,opt,end_name)
            print '合成完成'
        except Exception,e:
            print '合成失败'
            print e
    #print '进行截图保存'
    #name = ''+time.ctime().replace(' ','-')+'.png'
    #driver.save_screenshot(name)
    #print driver.page_source.encode('utf8')
    print 'end'
    time.sleep(10)
    #time.sleep(10)

    #i += 1
    #if i > 1:
    #    driver.close()
    #    driver.quit()

driver.close()
driver.quit()
