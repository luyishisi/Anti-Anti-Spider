#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   spider.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/12/12
#   语言：Python 2.7.x
#   操作：python Spider.py
#   功能:获取每天出现的招聘信息的公司数据
#         表结构()
#
#-------------------------------------------------------------------------
#coding:utf-8
import requests
import json
import time
#from write_sql import write2sqlite
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}

def get_jobs(keyword):
    jobs=[]
    page=1
    while True:
        js_data=requests.get('http://www.lagou.com/jobs/positionAjax.json?px=new&kd=%s&pn=%s&'%(keyword,page),headers=headers).text
        data=json.loads(js_data)
        data=data['content']['positionResult']['result']
        for item in data:
            job={}
            job['fromsite']='拉勾'
            job['id']=item['positionId']
            job['companyId']=item['companyId']
            job['positionType']=keyword
            job['positionName']=item['positionName']
            job['company']=item['companyFullName']
            job['salary']=item.get('salary')
            job['workYear']=item['workYear']
            job['education']=item['education']
            job['industryField']=item['industryField']
            job['companySize']=item['companySize']
            job['city']=item['city']
            job['financeStage']=item['financeStage']
            jobs.append(job)
        print(page,keyword,'ok')
        page+=1
        if page==31:
            break
        time.sleep(1)
    return jobs

def get_job_des(jobid):
    url='http://www.lagou.com/jobs/%s.html'%jobid
    html=requests.get(url,headers=headers,timeout=30).text
    des=BeautifulSoup(html,'lxml').find('dd',{'class':'job_bt'}).get_text()
    return des

def get_company_rate(companyid):
    url='http://www.lagou.com/gongsi/%s.html'%(companyid)
    html=requests.get(url,headers=headers,timeout=30).text
    rate=BeautifulSoup(html,'lxml').find('div',{'class':'reviews-top'}).find('span',{'class':'score'}).get_text()
    return rate

def main():
    keywords=[line.replace('\n','') for line in open('type.txt','r')]
    for keyword in keywords:
        jobs=get_jobs(keyword)
        result=[]
        for job in jobs:
            try:
                des=get_job_des(job['id'])
            except:
                des='-'
            try:
                rate=get_company_rate(job['companyId'])
            except:
                rate='-'
            job['jobDes']=des
            job['rate']=rate
            result.append(job)
            time.sleep(1)
#        write2sqlite(result,keyword)
        print result,keyword
        print(keyword,'ok')
main()
