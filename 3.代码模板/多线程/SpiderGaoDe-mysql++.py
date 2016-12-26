#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：SpiderGaoDe.py
#   版本：0.1
#   作者：***
#   日期：编写日期2016/12/7
#   语言：Python 2.7.x
#   操作：python SpiderGaoDe.py
#   功能：由IP获取高德地图中的经纬度
#         表结构(id, ip, lon_gd, lat_gd, datetime, flag)
#        接口已经失效 采用数据库批量插入优化等表结构优化
#-------------------------------------------------------------------------
import re ,os ,sys ,time ,json ,random ,MySQLdb ,requesocks ,threading

#--------------------------------------------------
#中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

session = requesocks.session()
# session.proxies = {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
#------------------------------------------------
#   可修改的全局变量参数--Start.
#Table = "TW_ALL_IP_BLOCK_GD_20161107_ip"# sys.argv[1] # 表名称需修改
#Table = "cn_ip_blk_single_ip_20161207_1_run"# sys.argv[1] # 表名称需修改
Table = "table"# sys.argv[1] # 表名称需修改
#HOST, USER, PASSWD, DB, PORT = '', '', '', '', 33306
HOST, USER, PASSWD, DB, PORT = '', '', '', '', 3306

#select_sql = "SELECT id, ip FROM %s WHERE flag IS NULL AND lat_gd IS NULL ORDER BY RAND() Limit 300000;"  # 可修改
select_sql = "SELECT id,ip FROM %s where flag = 3 limit 30000;" # 在数据库中i已经打乱了.
Update_sql = "UPDATE "+Table+" SET lon_gd=%s, lat_gd=%s, flag=%s WHERE id =%s;"  # 可修改

THREAD_COUNT =  50  #可修改
schedule = 0
ErrorList = []
WarnList = []
#   可修改全局变量参数--End.
#------------------------------------------------

class Handle_HTML(threading.Thread):
    """docstring for Handle_HTML"""
    def __init__(self, lock, ThreadID, tasklist, Total_TaskNum):
        super(Handle_HTML, self).__init__()
        self.lock = lock
        self.ThreadID = ThreadID
        self.tasklist = tasklist
        self.Total_TaskNum = Total_TaskNum

    def run(self):

        global schedule
        global ErrorList
        connect, cursor = ConnectDB()
        self.lock.acquire()
        print "The Thread tasklist number :", len(self.tasklist)
        self.lock.release()
        total = len(self.tasklist)
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        date_list = []
        i = 0
        for (id, ip) in self.tasklist:
            self.lock.acquire()
            time_Now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "Tread-%s:" % self.ThreadID, time_Now, "Already Completed:[%s] ,Also remaining:[%s]" % (schedule, self.Total_TaskNum - schedule)
            self.lock.release()

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
            URL = '接口已经失效' + str(random.random())
            #locator
            #print URL
            lon, lat = '0', '0'
            i += 1
            #print '*************************************',ip,i#,date_list
            try:
                time.sleep(random.uniform(0, 1))
                response = session.get(URL, headers=headers)
                #print response
                result = response.text.encode('utf-8')
                #print result
                result = json.loads(result)
                #print result
                if result.has_key('lat'):
                    lon, lat = result['lng'], result['lat']
                    #print result['cip'], lon, lat
                    #print Update_sql % (Table, lon, lat, 1, id)
                    #cursor.execute(Update_sql % (Table, lon, lat, 1, id))
                    #connect.commit()
                    #time.sleep(5)
                    date_list.append([lon,lat,1,id])
                else:
                    #print result['cip'], lon, lat
                    #lon = '0'
                    #lat = '0'
                    date_list.append([lon,lat,0,id])
                    #print Update_sql % (Table, lon, lat, 1, id)
                    #cursor.execute(Update_sql % (Table, lon, lat, 0, id))

            except Exception as e:
                print e
                time.sleep(random.uniform(0, 3))
                ErrorList.append("The ip is :[%s] Error:%s\n result:%s" %(ip, e, result))
            try:
                sql_num = int(random.uniform(200, 300)) #随机一个限制数,200-300 到则进行插入
                if(i >= sql_num):

                    i = 0
                    cursor.executemany(Update_sql , date_list)
                    connect.commit()
                    date_list = []
                    print 'uptime:10 ',time.ctime(),'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',sql_num
                #print 'uptime:300 ',time.ctime()
            except Exception as e:
                print Exception,e
                time.sleep(random.uniform(0, 3))
                #time.sleep(10)
                ErrorList.append("The ip is :[%s] Error:%s\n result:%s" %(ip, e, result))
                # print "The ip is :[%s] Error:%s\n result:%s" %(ip, e, result)
            self.lock.acquire()
            schedule += 1
            self.lock.release()
        cursor.executemany(Update_sql , date_list)#大爷的注释,,这里要保存一次
        connect.commit()
        connect.close()


def ConnectDB():
    "Connect MySQLdb and Print version."
    connect, cursor = None, None
    while True:
        try:
            connect = MySQLdb.connect(
                host=HOST, user=USER, passwd=PASSWD, db=DB, port=PORT, charset='utf8')
            cursor = connect.cursor()
            # cursor.execute("SELECT VERSION()")
            # data = cursor.fetchone()
            # print "Database version:%s\n"%data
            break
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
    return connect, cursor


def Thread_Handle(taskList, Total_TaskNum):

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
    global ErrorList
    global WarnList
    connect, cursor = ConnectDB()
    try:
        #cursor.execute( "create table DataBase_GD.%s as SELECT * FROM DataBase_GD.GD_BJ_10_day_0;" % Table )
        pass
    except Exception,e:
        print Exception,e
    cursor.execute(
        "SELECT COUNT(*) FROM %s WHERE flag = 3 ;" % Table)
		#create table DataBase_GD.GD_BJ_10_day_0 as SELECT * FROM DataBase_RTB.GD_BJ_10_day_0;
    TaskNum = cursor.fetchall()
    #TaskNum = 98914  #表的大小
    connect.close()
    if TaskNum[0][0] == 0:
        print "Warning:There is no need to do the task!!!"
    else:
        Total_TaskNum = int(TaskNum[0][0])
        while True:
            connect, cursor = ConnectDB()
            try:
                if cursor.execute(select_sql % Table):
                    rows = cursor.fetchall()
                    Thread_Handle(rows, Total_TaskNum)
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
