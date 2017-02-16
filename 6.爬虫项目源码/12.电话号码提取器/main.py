#coding:utf-8

#coding=utf-8
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
import re

if __name__ == '__main__':

    f = open('./name_list.txt','r')
    #f = open('./2.4.txt','r')
    #f = codecs.open('./2.5.txt.utf8','r')
    count = 0
    f_writer = open('end.txt','w')
    now_count = 0
    for i in f.readlines():
        count += 1
        #if count < 10:
        #print i
        search =  re.search(r'0?(13|14|15|18|17)[0-9]{9}',i)
        if search:
            now_count += 1
            print now_count,count,search.group(0),str(i)#, search.group(1)
            line = str(now_count)+':'+str(count)+' '+search.group(0)+' '+str(i)
            f_writer.write(line)
    f_writer.close()
             #print type(i),type(i.decode('utf8')).replace('',' ')
