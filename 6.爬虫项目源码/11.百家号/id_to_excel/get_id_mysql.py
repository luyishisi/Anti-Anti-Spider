# -*- coding: UTF-8 -*-
# 通过百度获取我们想要的id
# 缺点其实百度的每一个结果页面可以通过post来完成
# 运行方式 ：python3 get_id.py
import requests
import bs4
import re
from selenium import webdriver
import time
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

Table = " "#sys.argv[1]
THREAD_COUNT = 50 #需要修改
schedule = 0
HOST, USER, PASSWD, DB, PORT = '','','', '', 23306#需要修改

select_sql = "SELECT * FROM %s "
into_sql = ""

def ConnectDB():
    "Connect MySQLdb and Print version."
    connect, cursor = None, None
    count = 0
    while True:
        try :
            connect = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, port = PORT, charset ='utf8')
            cursor = connect.cursor()
            break
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            count += 1
            time.sleep(10)
            if count > 100:
                print 'error > 100 end'
                sys.exit(1)
    return connect, cursor
def changeurl(url):
    # req=requests.get('https://www.baidu.com/link?url=j7vtTkcM6jvJZ0RvWMtjslhKOY9lcrdlq8ruIP473AXuyfWomhFIgd0103xefJiWsR5n68jOkg1PjsLwV13d9a&wd=&eqid=cf53142600017e65000000045882cdfd')
    # https://www.baidu.com/link?url=w8wWEQMyVf0cD3TsKcn_pTQZ92cIqLqxVZKWFtT4rYJcESE_qfhKlPJg5B7OM2mXhZoSM1H0ogmCIgi4G2EkP_&wd=&eqid=aa2c3db90000bf4c0000000458831761
    req=requests.get(url+'&wd=')
    # time.sleep(1)
    regx  = r'http://baijiahao.baidu.com/u[\S]*"'
    pattern = re.compile(regx)
    match = re.findall(pattern,req.text)
    print(match)
    return match[0]

def getbaiduurl():
    urllist=set()
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/s?wd=site:(baijiahao.baidu.com) inurl: ( "http://baijiahao.baidu.com/u?app_id=" )')
    # print(source)//*[@id="page"]/a[11]，//*[@id="page"]/a[10]
    try:
        browser.find_element_by_xpath('//*[@id="page"]/a[11]').click()
    except Exception,e:
        print e
        browser.find_element_by_xpath('//*[@id="page"]/a[10]').click()
    time.sleep(2)
    while True:
        source = browser.page_source
        try:
            browser.find_element_by_xpath('//*[@id="page"]/a[11]').click()
            time.sleep(2)
        except:
            print('not find next_button may be for the page end!!!')
            break


        soup=bs4.BeautifulSoup(source,'lxml')
        for i in soup.findAll(class_='result c-container '):
            url=i.find(class_='t').find('a').get('href')

            if len(url) is 116:
                try:
                    url = changeurl(str(url))
                    print(url[36:-1])
                    print(len(urllist))
                    urllist.add(url)
                except:
                    print('error')
            #urllist.clear()
        time.sleep(0.5)
    print 'begin_save'
    with open('urllist_2_6_1.txt','w') as file:
        for i in urllist:
            file.write(i[36:-1])
            file.write('\n')
    file.close()

getbaiduurl()

if __name__ == '__main__':
    connect, cursor = ConnectDB()

    cursor.execute(sel_count %Table)

    TaskNum = cursor.fetchall()
