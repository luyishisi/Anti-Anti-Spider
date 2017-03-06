#coding:utf-8
import re
import time

import bs4
import requests
# from selenium import webdriver

class sobaidu():
    '''sobaidu类实现通过百度搜索获取真实的url并且把url写入数据库'''

    def __init__(self):
        self.KEYFILENAME = "keylist.txt"
        self.URLFILENAME = "urllist.txt"
        self.KEYLIST = set()
        self.URLLIST = set()
        self.URLFILE = open(self.URLFILENAME, 'w')

    def _readkey(self):
        '''读取百度搜索所需要的所有关键词'''
        with open(self.KEYFILENAME) as keyklistfile:
            for i in keyklistfile.readlines():
                self.KEYLIST.add(i)
    def _changeurl(self, url):
        '''百度搜索结果url转换为真实的url'''
        try:
            req = requests.get(url+'&wd=')
            # time.sleep(1)
            # print(req.text)
            regx = r'http[s]*://baijiahao.baidu.com/[\S]*id=[0-9]*'
            pattern = re.compile(regx)
            match = re.findall(pattern, req.text)
            return match[0]
        except Exception as e:
            print(e)

    def _writetomysql(self):
        '''将真实url写入数据库'''
        pass

    def _writetofile(self,url):
        self.URLFILE.write(url)
        self.URLFILE.write('\n')

    def sobaidu(self):
        '''调用以上函数解决我们的问题'''
        # browser = webdriver.Chrome()
        # # browser = webdriver.PhantomJS()
        headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.baidu.com",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    'postman-token': "d7d540ff-c479-210d-4d11-9b3deaba8395"
    }
        for key in self.KEYLIST:
            ''''doc'''
            now_num = 0
            # browser.implicitly_wait(30)
            try:
                # browser.get('https://www.baidu.com/s?wd=site:(baijiahao.baidu.com)' + key)
                req = requests.get('http://www.baidu.com/s?wd=site:(baijiahao.baidu.com)'+ key, headers=headers)
            except Exception as e:
                time.sleep(20)
                continue
            source = req.text
            soup = bs4.BeautifulSoup(source, 'lxml')
                # print('next_page')
            for i in soup.findAll(class_='result c-container '):
                url = i.find(class_='t').find('a').get('href')
                print(url)
                try:
                    self._writetofile(url)
                except Exception as e:
                    pass
            time.sleep(1)
def main():
    dsfsd = sobaidu()
    # strings = dsfsd._changeurl('https://www.baidu.com/link?url=w8wWEQMyVf0cD3TsKcn_pTQZ92cIqLqxVZKWFtT4rYJcESE_qfhKlPJg5B7OM2mXhZoSM1H0ogmCIgi4G2EkP_&wd=&eqid=aa2c3db90000bf4c0000000458831761')
    # print(strings)
    # # ###################### 奇怪的分割线 ###############
    dsfsd._readkey()
    print(len(dsfsd.KEYLIST))
    #########################  有点傻的分割线 #############
    dsfsd.sobaidu()
    # print(len(dsfsd.URLLIST))
    # for i in dsfsd.URLLIST:
    #     print(i)
    dsfsd.URLFILE.close()
if __name__ == '__main__':
    main()
    # getid()
