# -*- coding: UTF-8 -*-
# 通过百度获取我们想要的id
# 缺点其实百度的每一个结果页面可以通过post来完成
# 运行方式 ：python3 get_id.py
import requests
import bs4
import re
from selenium import webdriver
import time
import random

def changeurl(url):
    # req=requests.get('https://www.baidu.com/link?url=j7vtTkcM6jvJZ0RvWMtjslhKOY9lcrdlq8ruIP473AXuyfWomhFIgd0103xefJiWsR5n68jOkg1PjsLwV13d9a&wd=&eqid=cf53142600017e65000000045882cdfd')
    # https://www.baidu.com/link?url=w8wWEQMyVf0cD3TsKcn_pTQZ92cIqLqxVZKWFtT4rYJcESE_qfhKlPJg5B7OM2mXhZoSM1H0ogmCIgi4G2EkP_&wd=&eqid=aa2c3db90000bf4c0000000458831761
    try:
        req=requests.get(url+'&wd=')
        time.sleep(1)
        regx  = r'http://baijiahao.baidu.com/u[\S]*"'
        pattern = re.compile(regx)
        match = re.findall(pattern,req.text)
        print '#4',match
        return match[0]
    except Exception,e:
        print '#5',e
        return '0'

def getbaiduurl(key_list):
    #browser = webdriver.Chrome()
    browser = webdriver.PhantomJS()

    #urllist=set()
    #key = '军事'
    num = 5046
    for now_num_id in range(num,len(key_list)):
        key = key_list[now_num_id]
        print num,key
        num += 1
        urllist=set()
        now_num = 0
        browser.implicitly_wait(30)
        browser.get('https://www.baidu.com/s?wd=site:(baijiahao.baidu.com) '+ key )#+'inurl:( "http://baijiahao.baidu.com/u?app_id=" )')
        if now_num == 1:
            try:
                browser.find_element_by_xpath('//*[@id="page"]/a[10]').click()
                time.sleep(2)
            except Exception,e:
                print '#0',#e
                continue

        while True:
            now_num += 1
            source = browser.page_source
            soup=bs4.BeautifulSoup(source,'lxml')
            print 'next_page'
            for i in soup.findAll(class_='result c-container '):
                url=i.find(class_='t').find('a').get('href')
                print '#1',url
                try:
                    #url = changeurl(str(url))
                    #print(url[36:-1])
                    #print '#2',url,
                    #print (len(urllist))
                    urllist.add(url)
                except Exception,e:
                    print '#3 error',e
            time.sleep(1)
            if now_num > 1:
                try:
                    browser.find_element_by_xpath('//*[@id="page"]/a[11]').click()
                    time.sleep(1)
                except:
                    print('not find next_button may be for the page end!!!')
                    break
        #print urllist
        #存储部分
        print 'beging save ',len(urllist)
        with open('urllist4.txt','a') as file:
            for i in urllist:
                file.write(i)#[36:-1])
                file.write('\n')
        file.close()
        print 'end save '

if __name__ == '__main__':
    #main()
    count = 0
    idlist = []
    file = open('fingerDic.txt') # urllist.txt在你运行的目录下
    for i in file.readlines():
        idlist.append(i.replace('\n','').replace('\r',''))
        count += 1
    file.close()
    getbaiduurl(idlist)

