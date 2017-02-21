# -*- coding: UTF-8 -*-
# 通过百度获取我们想要的id
# 缺点其实百度的每一个结果页面可以通过post来完成
# 运行方式 ：python3 get_id.py
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import Image,re
from PIL import Image
import fileinput
from lxml import etree#
from sys import argv
import random

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

def changeurl(url):
    try:
        req=requests.get(url,timeout=5)
        #print 'end'
        #print req.text.encode('utf8')
        #req=requests.get(url+'&wd=')
        time.sleep(1)
        regx  = r'http[s]+://baijiahao.baidu.com/u[\S]app_id=[0-9]*'
        #regx  = r'手机百度'
        pattern = re.compile(regx)
        match = re.findall(pattern,req.text)
        print '#4',match
        return match[0]
    except Exception,e:
        print '#5',e
        return '0'

def url_get_id_usephantomjs(url,driver_pc):

    driver_pc.implicitly_wait(10)
    driver_pc.get(url)
    #driver_pc.save_screenshot('1.png')#//*[@id="followconModule"]/div/h3/div[2]/a/div/comment()[1]
    #print driver_pc.find_element_by_xpath("//div[@class='detail']/div[@class ='name']").text.encode('utf8')
    try:
        app_id = driver_pc.find_element_by_xpath("//div[@class='detail']/a[@class ='mth-pblog']").get_attribute("href")#.text.encode('utf8')
        return app_id
    except Exception,e:
        print e
        try:
            #changeurl(url)
            return '0'
        except Exception,e:
            return '0'

if __name__ == '__main__':

    driver_pc = webdriver.PhantomJS()
    file = open(r'./text/urllist5.txt','r')
    num = 0
    begin_num = int(argv[1])
    end_num = int(argv[2])
    for url in file.readlines():
        if begin_num >= num or num >= end_num:
            num += 1
            #print num
            continue
        else:
            num += 1
            print num,url,
            app_id = url_get_id_usephantomjs(url,driver_pc)
            time.sleep(0.5)
            print app_id
            print '********************'
            with open('./id_text/url_to_id'+str(begin_num)+'-'+str(end_num)+'.txt','a') as file_id:
                try:
                    file_id.write(app_id[37:53])
                    file_id.write('\n')
                except Exception,e:
                    print e
            file_id.close()

    file.close()
    driver_pc.quit()
