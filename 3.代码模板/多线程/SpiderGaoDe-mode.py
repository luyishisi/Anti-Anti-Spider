#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：SpiderGaoDe.py
#   版本：0.1
#   作者：***
#   日期：编写日期2016/6/22
#   语言：Python 2.7.x
#   操作：python SpiderGaoDe.py Table
#   功能：由IP获取地图中的经纬度
#         表结构(id, ip, lon_gd, lat_gd, datetime, flag)
#        本接口已经失效,
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
Table = "TW_ALL_IP_BLOCK_GD_20161107_ip"# sys.argv[1] # 表名称需修改
HOST, USER, PASSWD, DB, PORT = '127.0.0.1', 'name', 'passwd', 'TW_ISP', 3306

select_sql = "SELECT id, ip FROM %s WHERE flag IS NULL AND lat_gd IS NULL ORDER BY RAND() Limit 30000;"  # 可修改
Update_sql = "UPDATE %s SET datetime=now(), lon_gd='%s', lat_gd='%s', flag=%s WHERE id =%s;"  # 可修改

THREAD_COUNT = 50  # 可修改
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

        global schedule, ErrorList
        connect, cursor = ConnectDB()#建立链接
        self.lock.acquire()
        print "The Thread tasklist number :", len(self.tasklist)
        self.lock.release()
        total = len(self.tasklist)

        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

        for (id, ip) in self.tasklist:
            self.lock.acquire()#锁定
            time_Now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "Tread-%s:" % self.ThreadID, time_Now, "Already Completed:[%s] ,Also remaining:[%s]" % (schedule, self.Total_TaskNum - schedule) #？
            self.lock.release()#释放

            headers = {
                    'User-Agent': user_agent,
                    'Referer':'',
                    'X-Forwarded-For': ip  #通过伪造此字段来修改ip位置
                    }
            URL = '已经失效' + str(random.random())
            lon, lat = '', ''

            try:
                #---------------------------------
                # 发出请求并且抽取需要的数据并返回
                time.sleep(random.uniform(0, 1))#每个进程小休息一会
                response = session.get(URL, headers=headers)#发请求
                result = response.text.encode('utf-8')#改编码
                result = json.loads(result)
                if result.has_key('lat'):
                    lon, lat = result['lng'], result['lat']
                    print result['cip'], lon, lat
                    cursor.execute(Update_sql % (Table, lon, lat, 1, id))
                else:
                    cursor.execute(Update_sql % (Table, lon, lat, 0, id))
                connect.commit()
            except Exception as e:
                time.sleep(random.uniform(0, 3))
                ErrorList.append("The ip is :[%s] Error:%s\n result:%s" %(ip, e, result))
                # print "The ip is :[%s] Error:%s\n result:%s" %(ip, e, result)
            self.lock.acquire()  #？
            schedule += 1
            self.lock.release()
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
    cursor.execute(
        "SELECT COUNT(*) FROM %s WHERE flag IS NULL;" % Table)
    TaskNum = cursor.fetchall()
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
