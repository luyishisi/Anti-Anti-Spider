#-*-coding:utf-8 -*-
#网页url采集爬虫，给定网址，以及存储文件，将该网页内全部网址采集下，可指定文件存储方式
import requests,time
from lxml import etree

def Redirect(url):
    try:
        res = requests.get(url,timeout=10)
        url = res.url
    except Exception as e:
        print("4",e)
        time.sleep(1)
    return url

def baidu_search(wd,pn_max,save_file_name):

    #百度搜索爬虫，给定关键词和页数以及存储到哪个文件中，返回结果去重复后的url集合
    url = "https://www.baidu.com/s"
    return_set = set()
    for page in range(pn_max):
        pn = page*10
        querystring = {"wd":wd,"pn":pn}
        headers = {
            'pragma': "no-cache",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.8",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            }
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("!!!!!!!!!!!!",response.url)
            #解析html
            selector = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
        except Exception as e:
            print ("页面加载失败", e)
            continue

        with open(save_file_name,"a") as f:
            for i in range(1,10):
                try:
                    #根据属性href筛选标签
                    context = selector.xpath('//*[@id="'+str(pn+i)+'"]/h3/a[1]/@href')
                    print(len(context),context[0])
                    #跳转到获取的url，若可跳转则返回url
                    i = Redirect(context[0])
                    f.write(i)
                    return_set.add(i)
                    f.write("\n")
                except Exception as e:
                    print(i,return_set)
                    print("3",e)
    return return_set

if __name__ == '__main__':

    wd = "阿里巴巴 双十一"
    pn = 3
    save_file_name = "save_url.txt"
    return_set = baidu_search(wd,pn,save_file_name)
