import requests

url = "http://gs.amac.org.cn/amac-infodisc/api/pof/manager"

payload = "rand=0.8368381434843817&page=7&size=20"
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'connection': "keep-alive",
    'content-length': "2",
    'content-type': "application/x-www-form-urlencoded",
    'host': "gs.amac.org.cn",
    'origin': "http://gs.amac.org.cn",
    'referer': "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache",
    'postman-token': "ca812efb-74f2-eca7-5b65-073a461a7be1"
    }

#response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)



def t():
    #print '3',a
    if False:
        k()
        #global a
        pass
    print '2',a
    a += 1
    print '1',a

def k():
    print "!",a
    global a



if __name__ == '__main__':
    a = 1
    t()
    print a
