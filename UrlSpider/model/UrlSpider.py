#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：UrlSpider.py
#   版本：1
#   作者：ly
#   日期：编写日期2016/12/25
#   语言：Python 2.7.x
#   操作：python UrlSpider.py
#   功能：指定任务表，读取url，多线程采集
#         表结构(id, ip, lon_gd, lat_gd, datetime, flag)
#        采用数据库批量插入优化等表结构优化
#-------------------------------------------------------------------------
import re ,os ,sys ,time ,json ,random ,MySQLdb ,requesocks ,threading，requests

#--------------------------------------------------
#中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

#------------------------------------------------
# 代理以及tor设置。
session = requesocks.session()
# session.proxies = {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}

#------------------------------------------------
#   可修改的全局变量参数
Table = "table" # 表名称需修改
HOST, USER, PASSWD, DB, PORT = 'host', 'user', 'pass', 'dbname', 3306 # 数据库连接参数
select_sql = "SELECT id,url FROM %s where flag = 3 limit 30000;" # 在数据库中i已经打乱了.
Update_sql = "UPDATE "+Table+" SET date=%s, flag=%s WHERE id =%s;"  #数据存储

THREAD_COUNT =  50  #开启线程数
sql_num_base = 200 #自定义的执行批量插入的随机值基数，当此值为1时则每次获取数据均直接插入。
sql_num_add = 100 #自定义的随机值加数，平均而言，当单独一个线程执行sql_num_base+1/3*sql_num_add次数时执行插入
#   不可修改全局变量参数
#------------------------------------------------
schedule = 0 # 当前线程标志
ErrorList = []
WarnList = []

class Handle_HTML(threading.Thread):
    """docstring for Handle_HTML"""
    def __init__(self, lock, ThreadID, tasklist, Total_TaskNum):
        super(Handle_HTML, self).__init__()
        self.lock = lock
        self.ThreadID = ThreadID
        self.tasklist = tasklist
        self.Total_TaskNum = Total_TaskNum

    def run(self):

        global schedule, ErrorList
        connect, cursor = ConnectDB()
        self.lock.acquire()
        print "The Thread tasklist number :", len(self.tasklist)
        self.lock.release()
        total = len(self.tasklist)
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        date_list = []
        now_requests_num  = 0
        for (id, url) in self.tasklist:
            # -------------------------
            # 每个请求开始前进行进度说明，对线程上锁
            self.lock.acquire()
            time_Now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "Tread-%s:" % self.ThreadID, time_Now, "Already Completed:[%s] ,Also remaining:[%s]" % (schedule, self.Total_TaskNum - schedule)
            self.lock.release()

            # ------------------------
            # 可伪造的头部信息
            headers = {
                    'User-Agent': user_agent,
                    'Referer':'',
                    'X-Forwarded-For': ip,
                    'Accept':'*/*',
                    'Accept-Encoding':'gzip, deflate, sdch',
                    'Accept-Language':'zh-CN,zh;q=0.8',
                    'Cache-Control':'no-cache',
                    'Connection':'keep-alive',
                    'Host':'ditu.amap.com',
                    'Pragma':'no-cache',
                    'Referer':''
                    #User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36
                    }
            URL = url
            date = ''
            now_requests_num += 1
            #print '*************************************',ip,i#,date_list
            # -------------------------
            # 请求的具体请求部分
            try:
                # -- 发起
                time.sleep(random.uniform(0, 1))
                response = session.get(URL, headers=headers)
                result = response.text.encode('utf-8')

                # --- 请求解析--- 自定义使用正则还是xpath或etree,接口类数据可使用json
                if result:
                    date = result
                    date_list.append([date,1,id])# 用于批量插入，需要构建为一个列表,1作为flag存入
                else:
                    date_list.append([date,0,id])# 用于批量插入，需要构建为一个列表,0作为flag存入

            except Exception as e:
                print e
                time.sleep(random.uniform(0, 3))
                ErrorList.append("The ip is :[%s] Error:%s\n result:%s" %(ip, e, result))

            # ------------------------
            # 数据插入部分
            try:
                global sql_num_base
                sql_num = int(random.uniform(sql_num_base, sql_num_base + 100)) #随机一个限制数,200-300 到则进行插入
                if(now_requests_num >= sql_num):
                    now_requests_num = 0
                    cursor.executemany(Update_sql , date_list)
                    connect.commit()
                    date_list = []
                    print 'up',time.ctime(),'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',sql_num
            except Exception ,e:
                print e
                time.sleep(random.uniform(0, 3))
                ErrorList.append("The ip is :[%s] Error:%s\n result:%s" %(ip, e, result))
            # 切换线程
            self.lock.acquire()
            schedule += 1
            self.lock.release()
        cursor.executemany(Update_sql , date_list)#大爷的注释,,这里要保存一次
        connect.commit()
        connect.close()


def ConnectDB():
    "Connect MySQLdb "
    connect, cursor = None, None
    while True:
        try:
            connect = MySQLdb.connect(
                host=HOST, user=USER, passwd=PASSWD, db=DB, port=PORT, charset='utf8')
            cursor = connect.cursor()
            break
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
    return connect, cursor


def Thread_Handle(taskList, Total_TaskNum):
    '''多线程启动区域--无需修改'''
    global THREAD_COUNT
    lock = threading.Lock()
    WorksThread = []
    every_thread_number = len(taskList) / THREAD_COUNT
    if every_thread_number == 0:
        THREAD_COUNT = len(taskList)
        every_thread_number = 1

    for i in range(THREAD_COUNT):
        if i != THREAD_COUNT - 1:
            source_list = taskList[
                i * every_thread_number: (i + 1) * every_thread_number]
            Work = Handle_HTML(lock, i, source_list, Total_TaskNum)
        else:
            source_list = taskList[i * every_thread_number:]
            Work = Handle_HTML(lock, i, source_list, Total_TaskNum)
        Work.start()
        WorksThread.append(Work)
    for Work in WorksThread:
        Work.join()


def main():
    global ErrorList, WarnList
    connect, cursor = ConnectDB()

    # 统计表总行数,依据flag = 3
    try:
        cursor.execute("SELECT COUNT(*) FROM %s WHERE flag = 3 ;" % Table)
    except Exception,e:
        print e
    TaskNum = cursor.fetchall()
    connect.close()

    if TaskNum[0][0] == 0:
        print "Warning:There is no need to do the task!!!"
    else:
        Total_TaskNum = int(TaskNum[0][0])
        while True:
            connect, cursor = ConnectDB()# 建立数据库连接
            try:
                if cursor.execute(select_sql % Table):# 取任务url
                    rows = cursor.fetchall()
                    Thread_Handle(rows, Total_TaskNum)# 线程启动
                else:
                    break
            except Exception, e:
                print e
            connect.close()
    print "_____************_____"
    if ErrorList :
        for error in ErrorList:
            print error
    print "Error:", len(ErrorList), "Warning:",len(WarnList)

if __name__ == '__main__':
    print "The Program start time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start = time.time()
    main()
    print "The Program end time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "[%s]" % (time.time() - start)
    # raw_input("Please enter any key to exit!")
