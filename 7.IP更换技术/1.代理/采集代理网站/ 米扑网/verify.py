import requests
import sqlite3
import threading
import time

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
                self.update()
        except:
            self.delete()
        return

    def update(self):
        conn=sqlite3.connect('sqldb.db')
        cursor=conn.cursor()
        date=time.strftime('%Y-%m-%d %X', time.localtime())
        cursor.execute("update enableips set date=? where ip=?",(date,self.ip,))
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self):
        conn=sqlite3.connect('sqldb.db')
        cursor=conn.cursor()
        cursor.execute("delete from enableips where ip=?",(self.ip,))
        print('delete ',self.ip)
        cursor.close()
        conn.commit()
        conn.close()

def verify():
    conn=sqlite3.connect('sqldb.db')
    cursor=conn.cursor()
    rows=cursor.execute('select * from enableips')
    iplist=[]
    for row in rows:
        iplist.append(row[0])
    threadings=[]
    for ip in iplist:
        work=IsEnable(ip)
        work.setDaemon(True)
        threadings.append(work)
    for work in threadings:
        work.start()
    for work in threadings:
        work.join()

if __name__ == '__main__':
    while True:
        verify()
        time.sleep(600)
