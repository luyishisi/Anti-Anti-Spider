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
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

Table = ""#sys.argv[1]
THREAD_COUNT = 50 #需要修改
schedule = 0
HOST, USER, PASSWD, DB, PORT = '','','', 'IP_CN', 23306#需要修改

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
if __name__ == '__main__':
    idlist=[]
    count = 0
    id_set = set('')

    id_text_name_list = ['url_to_id.txt']
    #id_text_name_list = os.listdir()

    for name in id_text_name_list:
        if name.find('txt') != -1:
            file = open(name) # urllist.txt在你运行的目录下
            for i in file.readlines():
                idlist.append(i)
                id_set.add(i.replace('\n',''))
                #print count,i
                count += 1
            file.close()

    print len(id_set),count
    print id_set
    f = open('temp.txt','a')
    for i in id_set:
        print i
        f.writelines(i+'\n')
    f.close()

    # connect, cursor = ConnectDB()
    #
    # cursor.execute(sel_count %Table)
    #
    # TaskNum = cursor.fetchall()
