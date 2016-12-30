#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_so.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：发出请求并且解析
#
#-------------------------------------------------------------------------
import requests
import time,sys,json
import xlsxwriter

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()

def requests_post(key):
    url = "https://s.m.taobao.com/search"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"event_submit_do_new_search_auction\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"_input_charset\"\r\n\r\nutf-8\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"topSearch\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"atype\"\r\n\r\nb\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"searchfrom\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\nhome:redirect_app_action\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"from\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"q\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sst\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"n\"\r\n\r\n20\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"buying\"\r\n\r\nbuyitnow\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"m\"\r\n\r\napi4h5\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"abtest\"\r\n\r\n27\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"wlsort\"\r\n\r\n27\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"style\"\r\n\r\nlist\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"closeModues\"\r\n\r\nnav,selecthot,onesearch\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'accept': "application/json",
        'accept-encoding': "gzip, deflate, sdch, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cache-control': "no-cache",
        'cookie': "thw=ca; cna=mx3eEN4jylICAS9aUXroe7QT; uss=U7BF7ECyL2ASwrEOYQ44DNcPMBUz3pSobKdyq%2Byc6n8FghhgUKX%2BdwO8; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; ali_ab=171.15.132.56.1482321078252.3; uc2=wuf=http%3A%2F%2Fwww.umeng.com%2F%3Fspm%3D2013.1.1997523009.17.QKcgNw; cookie2=1c4616113d31ccff2a11ac55392b45c1; t=5e8eb89f88eaa0e6cc5ac88135841f4d; OUTFOX_SEARCH_USER_ID_NCOO=731539750.9226516; miid=423405037610384452; tkmb=e=E1DoNQOKQ8Bw4vFB6t2Z2ueEDrYVVa64gze6kOnl9rUYX8TY-NEwd6Vld1zxDwD4IfNVgZHErC7Qw2z4l0QSO7miPnyQLVs2v9hsW5EhbenF_tD4Y0_kjSP88i591npA_Qthylo3HFfXZs7UX6XuEPAd4QYtbexQJSdb3DTn-MUbi6LHOW70tnKirEH51Gw9pWV3XPEPAPgAvPM5QRELPMu0DvJ4SySS90WRxBXkWV7iC0Er_lIGgiIDeMwxoAFc-D2lLpi0SOqtD0dafC_ZEg&iv=0&et=1482556362; linezing_session=HWVtZf1l8XH0dACdMJQQDOt4_1482556828494E2ui_9; uc3=sg2=BYiIfEpsMbxtm040yzQn62r4dy8462CfLR73vjezc00%3D&nk2=&id2=&lg2=; hng=CN%7Czh-cn%7CCNY; tracknick=; mt=ci=0_0&cyk=2_1; v=0; _m_h5_tk=1d52cfb51a019fc6b3f3bcafcb88fc5a_1482910547070; _m_h5_tk_enc=37149113fb0caf06a0f086a605721964; _tb_token_=YfuOSRriSmBkwyRo5m4h; uc1=cookie14=UoW%2FX9Q1zQXCpw%3D%3D; JSESSIONID=299315B3B9143C57D3CEFD7E71B56B99; ___rl__test__cookies=1482995634939; l=AoWF82noU/G0VcAybR9piIJLFdq/Hzjl; isg=AhsbL2-dx8agsTsMpa_FVkRjqnlPnL4I5G5pIw1YqpsA7DDOkMBuQAkq9PYd",
        'pragma': "no-cache",
        'referer': "https://s.m.taobao.com/h5?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E7%9A%AE%E8%A3%A4%E7%94%B7&sst=1&n=20&buying=buyitnow",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'postman-token': "761c6c35-7ef9-7fbe-d235-859dd1ea4551"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def main(work):
    url = 'https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E7%9A%AE%E8%A3%A4%E7%94%B7&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page=1'
    body = requests.get(url)
    body = body.text.encode('utf8')

    dic_body = eval(body)
    #print type(dic_body)
    #print dic_body["RN"]
    for i in range(40):
        try:
            act = dic_body["listItem"][i]['act'] # 付款数
        except:
            act = ''
        try:
            area = dic_body["listItem"][i]['area'] # 地区
        except:
            area = ''
        try:
            auctionURL = dic_body["listItem"][i]['auctionURL'] # 商品url
        except:
            auctionURL = ''
        try:
            name = dic_body["listItem"][i]['name'] # 商品名
        except:
            name = ''
        try:
            nick = dic_body["listItem"][i]['nick'] # 店铺名
        except :
            nick = ''
        try:
            originalPrice = dic_body["listItem"][i]['originalPrice'] # 原始价格
        except:
            originalPrice = ''
        try:
            price = dic_body["listItem"][i]['price'] # 当前价格
        except :
            price =''
        try:
            pic_path = dic_body["listItem"][i]['pic_path'] # 当前价格
        except:
            pic_path = ''
        try:
            zkType = dic_body["listItem"][i]['zkType'] # 当前价格
        except:
            zkType = ''
        date = [ name, nick,act,price ,originalPrice,zkType,area,auctionURL,pic_path]
        #print len(date)
        num = i+2
        install_table(date,work,num)
    # 商品名 店铺 付款人数 当前价格 原始价格 优惠类型 地区 商品url  图片url  #
    # name nick act price originalPrice zkType area auctionURL pic_path

def install_table(date,work,i):
    #i = 2
    str_list = ['B','C','D','E','F','G','H','I','J','K']
    #global worksheet1
    work.write('A'+str(i),int(i)-1)
    for now_str,now_date in zip(str_list,date):
        #print now_str,now_date
        num = now_str+str(i)
        #print num,len(now_date)

        try:
            work.write(num,now_date)
        except Exception, e:
            print e




def create_table(name):
    name = name+'.xlsx'
    workbook   = xlsxwriter.Workbook(name)
    worksheet1 = workbook.add_worksheet()
    worksheet1.write('A1', 'ID')
    worksheet1.write('B1', u"商品名")
    worksheet1.write('C1', u'店铺')
    worksheet1.write('D1', u'付款人数')
    worksheet1.write('E1', u'当前价格')
    worksheet1.write('F1', u'原始价格')
    worksheet1.write('G1', u'优惠类型')
    worksheet1.write('H1', u'地区')
    worksheet1.write('I1', u'商品url')
    worksheet1.write('J1', u'图片url')
    worksheet1.write('K1', u'time')
    #workbook.close()
    print 'end'
    return worksheet1,workbook

if __name__ == '__main__':
    work,workbook = create_table('filename')
    main(work)
    workbook.close()
    print 'close'
