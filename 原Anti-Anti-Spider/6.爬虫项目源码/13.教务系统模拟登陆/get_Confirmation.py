import requests

def download_confirmation():

    url = "http://jiaowu.pdsu.edu.cn/sys/ValidateCode.aspx"
    for i in range(1,1000):
        querystring = {"t":str(i)}
        headers = {
            'accept': "image/webp,image/*,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, sdch",
            'accept-language': "zh-CN,zh;q=0.8",
            'connection': "keep-alive",
            'cookie': "ASP.NET_SessionId=jjlbi121br4kj145hhkwfj55",
            'host': "jiaowu.pdsu.edu.cn",
            'referer': "http://jiaowu.pdsu.edu.cn/_data/index_LOGIN.aspx",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            'x-forwarded-for': "175.51.151.187",
            'x-real-ip': "175.51.151.187",
            'cache-control': "no-cache",
            }

        print i,'begin',
        try:
            response = requests.request("GET", url, headers=headers, params=querystring,timeout = 20)
            f = open('./img1/'+str(i)+'.png','w')
            f.write(response.content)
            f.close()
            print i,'end'
        except Exception,e:
            print e
    #print(response.text)

if __name__ == '__main__':
    download_confirmation()
    #main()
