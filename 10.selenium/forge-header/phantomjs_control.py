

import os,re,time,MySQLdb,MySQLdb.cursors,urllib2,random
import requests
for i in range(300,400):
    common = 'phantomjs' + ' phantomjs.js ' + str(i)
    print time.ctime(),common
    str_body =  str(os.popen(common).read())
