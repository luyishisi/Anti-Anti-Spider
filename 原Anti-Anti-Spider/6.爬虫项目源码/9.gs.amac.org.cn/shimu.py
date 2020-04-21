from selenium import webdriver
import time
import bs4
urllist = set()
browser = webdriver.Chrome()
browser.get('http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html')
time.sleep(5)
browser.get('http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html')

nextButton = browser.find_element_by_xpath(
    '//*[@id="managerList_paginate"]/a[3]')
t = browser.find_element_by_xpath(
    '//*[@id="managerList_length"]/label/select/option[4]')
t.click()
time.sleep(3)
i = 1
while True:
    soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
    if len(soup.findAll('tbody')[4].findAll('tr')) < 100: # 有一个BUG最后一个页面没有抓取就结束了
        break
    for tmp in soup.findAll('tbody')[4].findAll('tr'):
        urllist.add(tmp.findAll('td')[1].find('a').get('href'))
    nextButton.click()
    time.sleep(2)
    print(i)
    print(len(urllist))
    i = i + 1
    time.sleep(5)
