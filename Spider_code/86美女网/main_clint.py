#coding:utf-8
#完成通用爬虫，抓取一个页面队列中所有图片

import requests
import re
import time
#from redis import Redis

headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

def download(url,name,now,maxnum):
    for i in range(now,maxnum):
        try:
            now_url = url+str(i)+".html"
            print now_url
            #time.sleep(10)
            r = requests.get(now_url,headers=headers,timeout = 50)
            img_url_list = re.findall('http://img.sc601.com/photo_files/news/.*.jpg',r.text)[0]
            r = requests.get(img_url_list,headers=headers,timeout = 50)
            print url,name,type(name)
            f = open(unicode('./pic/'+name+str(i)+'.jpg',"utf-8"),"w")
            #f = open('./pic/'+name.decode('utf8')+'.jpg','wb')
            f.write(r.content)
            f.close()
        except Exception,e:
            print Exception,":",e
    return -1

def push_redis_list(num):
    for i in range(100):
        try:
            num = num+i;#抓取的取件仅在num+100--num+200之间
            url = "http://m.17786.com/"+str(num)+"_1.html"

            img_url = requests.get(url,headers = headers, timeout=30)
            name = re.findall('<title>.*</title>',img_url.text)[0]
            name = name.replace('<title>','')
            name = name.replace('</title>','.jpg')
            name = name.replace('/',':')
            #name = name.replace('(','')
            #name = name.replace(')','')
            name = name.replace('_','')
            name = name.replace(u'美女86','')
            name = name.encode('utf8')

            pagenum = name.split(':')[1].split(')')[0]
            print pagenum

            #print img_url.text
            print name
            #img_url_list = re.findall('http://img.sc601.com/photo_files/news/.*.jpg',img_url.text)[0]
            #url = url.replace('.jpg',"")
            url = "http://m.17786.com/"+str(num)+"_"
            #print img_url_list
            maxnum = int(pagenum)
            download(url,name,1,maxnum)
        except:
            time.sleep(10)
            continue
        #time.sleep(10)

    return 0

if __name__ == '__main__':
    print "begin"
    push_redis_list(6952)#开启则加任务队列.其中的值请限制在5400以内。不过是用于计算页码的

    #get_big_img_url()#开启则运行爬取任务
