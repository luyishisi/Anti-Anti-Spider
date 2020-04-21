import requests

url = "https://v4.passport.sohu.com/i/verify/mobile/bind"

querystring = {"mobile":"18128867646","log":"1","appid":"114105","callback":"passport403_cb1530605085935","_":"1530605158988"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "*/*",
    'cache-control': "no-cache",
    'authority': "v4.passport.sohu.com",
    'cookie': "vjuids=-92e61006.1600684a143.0.732412ee52d4d; vjlast=1511937844.1511937844.30; sohutag=8HsmeSc5NCwmcyc5NCwmYjc5NSwmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NCwmaSc5NCwmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0; gidinf=x099980109ee0d4ea94ac684f000b9f448844dee7c64; t=1529143081745; IPLOC=CN4400; SUV=1707131758470322; reqtype=pc",
    'referer': "http://www.56.com/",
    'postman-token': "96365418-b741-261e-54a4-c5e6725b44aa"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
