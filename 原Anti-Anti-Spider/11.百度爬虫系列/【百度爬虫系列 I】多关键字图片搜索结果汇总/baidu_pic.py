# -*- coding:utf-8 -*-
import requests,json
url = "https://image.baidu.com/search/acjson"


"""
获取图片的所有urls,存入set集合中去重，存在urls.txt中
"""
def get_urls(key,sum):
    #请求头
    url = "https://image.baidu.com/search/index"
    headers = {
        'cookie': "td_cookie=2373937907; BDqhfp=%E6%B5%B7%E8%BE%B9%26%260-10-1undefined%26%260%26%261; BAIDUID=E26F8B2E16E037DF58FED1FDEAD8A636:FG=1; BIDUPSID=E26F8B2E16E037DF58FED1FDEAD8A636; PSTM=1506000312; pgv_pvi=229598208; td_cookie=2463294905; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E6%B5%B7%E8%BE%B9%22%2C%22%E6%B5%B7%E5%B2%B8%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'accept': "text/plain, */*; q=0.01",
        'referer': "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%B5%B7%E8%BE%B9&oq=%E6%B5%B7%E8%BE%B9&rsp=-1",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'postman-token': "c1717c49-7d6f-b452-0005-026e525e7b43"
        }
    #pn控制页数
    pn = 0
    n = 0
    pages = 1
    flag = True
    s = set()

    #循环获取url
    for pn in range(0,21):
        print "pn=" + str(pn*30)
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=" + key + "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=" + key + "&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=" + str(pn*30) + "&rn=30"
        #url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={key}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={key}&face=0&istype=2nc=1&pn={pn}&rn=60"
        #url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+key+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%B5%B7%E8%BE%B9&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn="+str(pn*30)+"&rn=30"
        #print url
        r = requests.get(url,headers=headers).text.encode("utf-8")
        try:
            dictinfo = json.loads(r)
            #每页30张
            for i in range(0,30):
                #print i
                if n == sum:
                    flag = False
                else:
                    temp = dictinfo["data"][i]["thumbURL"]
                    n = n + 1
                    s.add(str(temp)+"\n")
        except:
            print "请求发送失败重试"

    print len(s)
    f = open("urls.txt","w")
    for url in s:
        f.write(url)
    f.close()
    print "get_urls 完成"


#将图片写在pic文件夹
def write_pics(SavePath,sum):

    f = open("./urls.txt","r")
    m = 1

    for url in f:
        Path = SavePath + str(m) +".jpg"
        f1 = open(Path,"wb")
        r = requests.get(url)
        f1.write(r.content)
        #print m
        m = m + 1

    f1.close()
    print "write_pics 完成"

def get_class(name):
    name = name.split("|")
    print len(name)

    for index in range(0,len(name)):
        print "mingzi=" + name[index]
        SavePath = "./snow/"+ str(name[index]) + "_"
        print SavePath
        get_urls(name[index], sum)
        write_pics(SavePath,sum)
        print "a"


if __name__=="__main__":
    sea = "海边|海岸|沿海"
    tree = "山林|树林|森林"
    road = "公路|道路|小路|马路"
    snow ="雪景|雪地|冬天景色"
    town ="小镇|小镇风光|小镇建筑风景"
    sum = 600
    get_class(snow)
