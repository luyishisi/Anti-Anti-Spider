# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:51:35 2016

@author: weiya
"""

#import urllib2
from bs4 import BeautifulSoup
#import lxml.html
import re
import json
import base64
import requests
import sqlite3
import datetime
import urllib
import random
import httplib
import companyList
import user_agents
import os
import sys
import time
#from account2 import account
#import cookielib

class SinaCrawl():
    
    def __init__(self,keyword,tm_start,tm_delta,conn,session):
        #self.myheader = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        self.url = 'http://s.weibo.com/weibo/'
        self.URL = self.url + urllib.quote(keyword) + '&typeall=1&suball=1&timescope=custom:'+str(tm_start)+':'+str(tm_start)+'&Refer=g'
        self.myheader = {'User-Agent':"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0"}
        # self.myheader = self.getHeader()
        self.conn = conn
        self.session = session

                         
    def getHeader(self):
        #fUserAgent = open('UserAgent.txt')
        #content = fUserAgent.read()
        #pattern = re.compile('User-Agent:.*[^\n]')
        #UserAgentList = pattern.findall(content)
        #UserAgent = UserAgentList[random.choice(range(len(UserAgentList)))]
        #user_agent1, user_agent2 = UserAgent.split('User-Agent:')
        #Referers =['https://www.baidu.com/', 'http://http://s.weibo.com/weibo/%25E7%258E%258B%25E9%25B8%25A5%2B%25E5%259B%259E%25E5%25BA%2594&Refer=STopic_top',
        #           'https://www.google.com/','https://www.hao123.com/','http://www.sogou.com']
        #referer = random.choice(Referers)
        user_agent = random.choice(user_agents.agents)
        myheader = {'User-Agent':user_agent}
        return myheader
        
    def login(self):
        self.username = base64.b64encode(self.username.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": self.username,
            "service": "sso",
            "sp": self.password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
        session = requests.Session()
        res = session.post(loginURL, data = postData)
        jsonStr = res.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print("Login Success!")
            
            cookies = session.cookies.get_dict()
            cookies = [key + "=" + value for key, value in cookies.items()]
            cookies = "; ".join(cookies)
            session.headers["cookie"] = cookies
        else:
            print("Login Failed，resons： %s" % info["reason"])
        return session
        
    def getPublicIp(self):
        url = 'http://1212.ip138.com/ic.asp'
        try:
            page = self.session.get(url).content
            return re.search('\d+.\d+.\d+.\d+',page).group(0)
        except:
            return 0
            
    def getWeiboContent(self):
        weiboContent = ""
        try:
            req = self.session.get(self.URL, headers = self.myheader)
            if req.status_code == 200:
                print 'This session work.'
                print 'The current Ip is ' + self.getPublicIp()
            else:
                print 'This session not work with code 200.'
                return False
        except:
            print 'This session not work.'
            return False
        try:
            page = req.content

        except httplib.IncompleteRead:
            print 'Incompleted!'
            return False
# try to use phantomjs
#        cmd = 'phantomjs' + ' request.js ' + self.URL + ' '+ str(self.myheader)
#        str_body =  str(os.popen(cmd).read())
#        page = str_body.split('\nbegin\nStatus: success\n')[1]
        soupPage = BeautifulSoup(page, 'lxml')
        numList = soupPage.find_all('script')
        if len(numList) == 0:
            print 'you may need to input an access code'
            return False
        for i in range(0, len(numList)):
            IsSearch = re.search(r"\"pid\":\"pl_weibo_direct\"", str(numList[i]))
            if IsSearch == None:
                continue
            else:
                weiboContent = str(numList[i])
                break
        return weiboContent
        
    def getWeiboHtml(self):
        weiboContent = self.getWeiboContent()
        if weiboContent == "":
            print 'WeiboContents are empty. You may need to input an access code.'
            return False
        elif weiboContent == False:
            return False
        
        # in case some empty json element
        substr = re.compile("\[\]")
        weiboContent = substr.sub("\"NULL\"", weiboContent)
        
        substr1 = re.compile("^.*STK.pageletM.view\\(")
        substr2 = re.compile("\\)$")
        substr4 = re.compile(r'\[')
        substr5 = re.compile(r'\]')
        substr6 = re.compile(r'\)</script>$')
        weiboContent = substr1.sub("", weiboContent)
        weiboContent = substr2.sub("", weiboContent)
        weiboContent = substr4.sub("", weiboContent)
        weiboContent = substr5.sub("", weiboContent)
        weiboContent = substr6.sub("", weiboContent)
        try:
            weiboJson = json.loads(weiboContent)
        except:
            print 'Json Error!'
            return -3
        if weiboJson == None:
            print 'you may need to input an access code'
            return True
            
        weiboHtml = weiboJson["html"]
        return weiboHtml
    
    def getData(self,weiboHtml):
        #weiboHtml = self.getWeiboHtml()
        soup = BeautifulSoup(weiboHtml, 'lxml')
        Noresult = soup.find_all('div',{'class':'pl_noresult'})
        if len(Noresult) != 0:
            print 'NO result for the current search criteria.'
            # No result
            return 0
        
        WeiboItemAll =  soup.find_all('div',{'action-type':'feed_list_item'})
        WeiboItemFeed = soup.find_all('ul', {'class':'feed_action_info feed_action_row4'})
        WeiboItemContent = soup.find_all('p',{'class':'comment_txt'})
        #WeiboItemPraised = soup.find_all('i',{'class':'W_ico12 icon_praised_b'})
        #WeiboItemComment = soup.find_all('a',{'suda-data':re.compile(r"key=tblog_search_weibo&value=weibo_ss_[0-9]+_p$")})
        #WeiboItemForward = soup.find_all('a',{'suda-data':re.compile(r"key=tblog_search_weibo&value=weibo_ss_[0-9]+_z$")})
    #    if len(WeiboItemContent) == 20 and WithHeader == False:
    #        return 1
        if len(WeiboItemContent) != len(WeiboItemAll):
            return 3
        elif len(WeiboItemContent) != len(WeiboItemFeed):
            return 3
        elif len(WeiboItemAll) != len(WeiboItemFeed):
            return 3
            
        for i in range(0, len(WeiboItemContent)):
            soupContent = BeautifulSoup(str(WeiboItemContent[i]), "lxml")
            soupAll = BeautifulSoup(str(WeiboItemAll[i]), "lxml")
            soupFeed = BeautifulSoup(str(WeiboItemFeed[i]), "lxml")
            
            mid = str(soupAll.div.attrs['mid'])
            STR = ""
            for string in soupContent.strings:
                STR += string
            content = STR
    #        print content
    #        content = str(soupContent.body.p.contents[0])
            when = soupAll.find('a',{'class':'W_textb'})
    #        if when.next_sibling == None:
    #            by = 'NULL'
    #        elif when.next_sibling.next_sibling == None:
    #            by = str(when.next_sibling.string)
    #        else:
    #            by = str(when.next_sibling.next_sibling.string)
            weibotime = str(when['title'])
    #        print weibotime
            #time = datetime.datetime.strptime(str(when['title']), "%Y-%m-%d %H:%M")
            WeiboItemPraised = soupFeed.ul.contents[7]
            WeiboItemComment = soupFeed.ul.contents[5]
            WeiboItemForward = soupFeed.ul.contents[3]
    
            if WeiboItemPraised.contents[0].contents[0].contents[1].string == None:
                praised = 0
            else:
                praised = int(str(WeiboItemPraised.contents[0].contents[0].contents[1].string))
            if len(WeiboItemComment.contents[0].contents[0].contents) == 1:
                comment = 0
            else:
                comment = int(str(WeiboItemComment.contents[0].contents[0].contents[1].string))
            if WeiboItemForward.contents[0].contents[0].contents[1].string == None:
                forward = 0
            else:
                forward = int(str(WeiboItemForward.contents[0].contents[0].contents[1].string))
            weiboitem = (mid, content, weibotime, praised, comment, forward)
            self.conn.execute("INSERT INTO weibo VALUES(?,?,?,?,?,?)", weiboitem)
            self.conn.commit()
        return 2
    
    def run(self):
        page = self.getWeiboHtml()
        if page == False:
            return -1
        elif page == -3:
            return -3
        flag = self.getData(page)
        if flag == 0:
            print 'No result.'
        elif flag == 2:
            print 'Complete!'
        elif flag == 3:
            print 'unknown error'
        return flag
        
#        if page == False:
#            proxyrow = self.cursor.fetchone()
#            if proxyrow == None:
#                print 'The proxy ip has used up.'
#                break
#            ip = proxyrow[0]
#            port = proxyrow[1]
#            proxy = {'http':ip+':'+port}
#            session = requests.Session()
#            session.proxies = proxy
#            print 'Try to use proxy: '+ip+':'+port

def CreateWeiboTable(db_name):
    conn = sqlite3.connect(db_name)
    try:
        create_tb_sql = '''
        CREATE TABLE IF NOT EXISTS weibo
        (mid TEXT,
        content TEXT,
        time TEXT,
        praised INTEGER,
        comment INTEGER,
        forward INTEGER);
        '''
        conn.execute(create_tb_sql)
    except:
        print 'CREATE table failed'
        return False
    conn.commit()
    conn.close()
    
def main(companyId, ferror):
    tm_start = datetime.date(2011,1,1)
    tm_delta = datetime.timedelta(days=1)
    tm_end = datetime.date(2015,12,31)
    keyword = companyList.company[companyId]
#    keyword = '同济科技'
    print 'Begin Crawl company' + keyword + '.'*10
    dbname = 'company'+ str(companyId).zfill(4)+'.db'
    CreateWeiboTable(dbname)
    conn = sqlite3.connect(dbname)
#    connProxy = sqlite3.connect('proxy5.db')
#    query_sql = '''
#    select IP,PORT from PROXY;
#    '''
#    cursor = connProxy.execute(query_sql)
    print tm_start
    session = requests.Session()
    iters = 0
    while tm_start < tm_end:
        if iters >15:
            try:
                os.popen('rasdial /disconnect').read()
                print 'Disconnect succeed!'
            except:
                continue
            time.sleep(15)
            try:
                # rasdial weiya USERNAME PASSWORD
                os.popen('rasdial weiya 051311152401 69453014').read()
                time.sleep(2)
                print 'Connect succeed!'
            except:
                continue
            iters = 0
            
#        keyword = random.choice(companyList.company)
#        time.sleep(random.uniform(0.1,0.5))
#        loginAccount = account[random.choice(range(len(account)))]
#        loginAccount = account[len(account)-1]
        sinaCrawl = SinaCrawl(keyword,tm_start,tm_delta,conn,session)
        flag = sinaCrawl.run()
        if flag == -1:
#            proxyrow = cursor.fetchone()
#            if proxyrow == None:
#                print 'The proxy ip has used up'
#                break
#            ip = proxyrow[0]
#            port = proxyrow[1]
#            proxy = {'http':'http://'+ip+':'+port}
#            print 'Try proxy:'+ip+':'+port
#            session = requests.Session()
#            session.proxies = proxy
            iters = iters + 1
            continue
        elif flag == 0:
            tm_start = tm_start + tm_delta
            print tm_start
        elif flag == 2:
            tm_start = tm_start + tm_delta
            print tm_start
        elif flag == 3:
            ferror.write('--------------------\n')
            ferror.write(str(companyId))
            ferror.write('length error happen on %s' %tm_start)
            tm_start = tm_start + tm_delta
            print tm_start
        elif flag == -3:
            ferror.write('--------------------\n')
            ferror.write(str(companyId))
            ferror.write(' Json error happen on %s' %tm_start)
            tm_start = tm_start + tm_delta
            print 'Json error, but I dont konw why yet.'
            print tm_start
        print '.'*20
        iters = iters + 1
    return 1

if __name__ == '__main__':
    companyId = int(sys.argv[1])
    main(companyId)
        
    
            
            
