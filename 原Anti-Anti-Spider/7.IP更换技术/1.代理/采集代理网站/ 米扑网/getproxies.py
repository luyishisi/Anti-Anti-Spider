import requests
import re
from bs4 import BeautifulSoup
import sqlite3
import threading
import time
from mimvp.mimvpproxy import mimvp_proxy

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

class IsEnable(threading.Thread):
    def __init__(self,ip):
        super(IsEnable,self).__init__()
        self.ip=ip
        self.proxies={
        'http':'http://%s'%ip
        }

    def run(self):
        try:
            html=requests.get('http://httpbin.org/ip',proxies=self.proxies,timeout=5).text
            result=eval(html)['origin']
            if len(result.split(','))==2:
                return
            if result in self.ip:
                self.insert_into_sql()
        except:
            return

    def insert_into_sql(self):
        conn=sqlite3.connect('sqldb.db')
        cursor=conn.cursor()
        try:
            date=time.strftime('%Y-%m-%d %X', time.localtime() )
            cursor.execute("insert into enableips(ip,date) values(?,?)",(self.ip,date,))
            print(self.ip)
        except:
            conn.close()
            return
        cursor.close()
        conn.commit()
        conn.close()


def get_from_ipcn():
    urls=['http://proxy.ipcn.org/proxya.html','http://proxy.ipcn.org/proxya2.html','http://proxy.ipcn.org/proxyb.html','http://proxy.ipcn.org/proxyb2.html']
    for url in urls:
        try:
            html=requests.get(url,timeout=30).text
        except:
            continue
        ips=re.findall('\d+\.\d+\.\d+\.\d+:\d+',html)
        threadings=[]
        for ip in ips:
            work=IsEnable(ip)
            work.setDaemon(True)
            threadings.append(work)
        for work in threadings:
            work.start()

def get_from_xicidaili():
    urls=['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nn/2','http://www.xicidaili.com/wn/']
    for pageurl in urls:
        try:
            html=requests.get(pageurl,headers=headers,timeout=30).text
        except:
            continue
        table=BeautifulSoup(html,'lxml').find('table',id='ip_list').find_all('tr')
        iplist=[]
        for tr in table[1:]:
            tds=tr.find_all('td')
            ip=tds[1].get_text()+':'+tds[2].get_text()
            iplist.append(ip)
        threadings=[]
        for ip in iplist:
            work=IsEnable(ip)
            work.setDaemon(True)
            threadings.append(work)
        for work in threadings:
            work.start()

def get_from_kxdaili():
    urls=['http://www.kxdaili.com/dailiip/1/%s.html','http://www.kxdaili.com/dailiip/3/%s.html']
    for url in urls:
        page=1
        while page<=10:
            try:
                html=requests.get(url%(page),headers=headers,timeout=30).text.encode('ISO-8859-1').decode('utf-8','ignore')
                page+=1
            except:
                continue
            try:
                table=BeautifulSoup(html,'lxml').find('table').find_all('tr')
            except:
                continue
            iplist=[]
            for tr in table[1:]:
                tds=tr.find_all('td')
                ip=tds[0].get_text()+':'+tds[1].get_text()
                iplist.append(ip)
            threadings=[]
            for ip in iplist:
                work=IsEnable(ip)
                work.setDaemon(True)
                threadings.append(work)
            for work in threadings:
                work.start()

def get_from_66ip():
    urls=['http://www.66ip.cn/nmtq.php?getnum=600&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip']
    for pageurl in urls:
        try:
            html=requests.get(pageurl,headers=headers,timeout=30).text
        except:
            continue
        iplist=re.findall('\d+\.\d+\.\d+\.\d+:\d+',html)
        threadings=[]
        for ip in iplist:
            work=IsEnable(ip)
            work.setDaemon(True)
            threadings.append(work)
        for work in threadings:
            work.start()

def get_from_mimvp():
    iplist=mimvp_proxy()
    threadings=[]
    for ip in iplist:
        work=IsEnable(ip)
        work.setDaemon(True)
        threadings.append(work)
    for work in threadings:
        work.start()

if __name__ == '__main__':
    conn=sqlite3.connect('sqldb.db')
    cursor=conn.cursor()
    cursor.execute('create table if not exists enableips(ip char(50) primary key,date char(50))')
    conn.commit()
    conn.close()
    while True:
        try:
            get_from_ipcn()
        except:
            print('get_from_ipcn','failed')
        try:
            get_from_kxdaili()
        except:
            print('get_from_kxdaili','failed')
        try:
            get_from_xicidaili()
        except:
            print('get_from_xicidaili failed')
        try:
            get_from_66ip()
        except:
            print('get_from_66ip failed')
        try:
            get_from_mimvp()
        except:
            print('get_from_mimvp failed')
        time.sleep(300)
