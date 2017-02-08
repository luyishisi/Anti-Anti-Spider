# -*- coding: UTF-8 -*-
import re ,os ,sys ,time ,json ,random ,MySQLdb ,requesocks ,threading
import requests,json
import subprocess
from threading import Timer
begin_id = 10100039

for i in range(10):
    try:
        id = begin_id+i
        url = '"http://www.ppdai.com/list/'+str(id)+'"'
        output = str(id)+'png'
        print url,output
        cmd = ["phantomjs", "rasterize.js",url,output]
        ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        kill = lambda process: process.kill()
        my_timer = Timer(10, kill, [ping])
        #time.sleep(10)
        try:
            my_timer.start()
            str_body, stderr = ping.communicate()
            print str_body#print time.ctime()
            my_timer.cancel()
        except Exception,e:
            print e
            str_body=''

    except Exception,e:
        print e
