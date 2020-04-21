#coding:utf-8
#百度搜索爬虫，给定关键词和页数以及存储到哪个文件中，返回结果去重复后的url集  合
# 网页url采集爬虫，给定网址，以及存储文件，将该网页内全部网址采集下，可指定文件存储方式
import requests,time
from lxml import etree
"""
    url:给定的url
    save_file_name:为url存储文件
"""
def Redirect(url):
    try:
        res = requests.get(url,timeout=10)
        url = res.url
    except Exception as e:
        print("4",e)
        time.sleep(1)
    return url

def requests_for_url(url, save_file_name, file_model):
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
        response = requests.request("GET", url, headers=headers)
        selector = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
    except Exception as e:
        print ("页面加载失败", e)

    return_set = set()
    with open(save_file_name,file_model) as f:
        try:
            context = selector.xpath('//a/@href')
            for i in context:
                try:
                    if i[0] == "j":
                        continue
                    if i[0] == "/":
                        print i
                        i = url+i.replace("/","");
                    f.write(i)
                    f.write("\n")
                    return_set.add(i)
                    print(len(context),context[0],i)
                except Exception as e:
                    print("1",e)
        except Exception as e:
            print("2",e)
    return return_set

if __name__ == '__main__':
     # 网页url采集爬虫，给定网址，以及存储文件，将该网页内全部网址采集下，可指定文件存储方式
     url = "http://news.baidu.com/"
     save_file_name = "save_url_2.txt"
     return_set = requests_for_url(url,save_file_name,"a") #“a”:追加
     print(len(return_set))
