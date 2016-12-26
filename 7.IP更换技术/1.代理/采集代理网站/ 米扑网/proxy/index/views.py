from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.
def index(requests):
    try:
        page=int(requests.GET['page'])
    except:
        page=1
    try:
        num=int(requests.GET['num'])
    except:
        num=1
    iplist=enable_ip(page=page,num=num)
    return HttpResponse(str(iplist))

def enable_ip(page,num):
    conn=sqlite3.connect('sqldb.db')
    cursor=conn.cursor()
    rows=cursor.execute('select * from enableips')
    iplist=[]
    for row in rows:
        item={}
        item['ip']=row[0]
        item['update_date']=row[1]
        iplist.append(item)
    length=len(iplist)
    start=(page-1)*num
    end=page*num
    if start>=length:
        start=length-1
    if end>=length:
        end=length-1
    return iplist[start:end]
