#coding:utf-8
import requests

url = "http://blog.csdn.net/xunalove/comment/submit"

querystring = {"id":"54948790"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"commentid\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n写的不错，我来看看\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"replyId\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'connection': "keep-alive",
    'content-length': "109",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'host': "blog.csdn.net",
    'origin': "http://blog.csdn.net",
    'referer': "http://blog.csdn.net/xunalove/article/details/54948790",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    'x-forwarded-for': "175.51.151.188",
    'x-real-ip': "175.51.151.188",
    'x-requested-with': "XMLHttpRequest",
    'cookie': "bdshare_firstime=1482074386697; uuid_tt_dd=2876793974890581118_20161218; _JQCMT_ifcookie=1; _JQCMT_browser=f6435c23260ef40cd7f7e91eb576bb77; OUTFOX_SEARCH_USER_ID_NCOO=137446819.53926876; uuid=c5874c71-9d0f-4604-a074-d5ae17bae98a; _ga=GA1.2.1503044291.1482220609; UserName=a83533774; UserInfo=8BqULP2%2BFlHA%2BWQ49z9UMSUt1IKLSdAZprXd7ViHIQtBFKSYvNDJ1G4gBYKbI6lZveNzLiHt%2Bh%2BBDCGQ5TkuICkR65ji2LMUyvERYDotyZmKk6cuvToAgVYLFvDmsALA; UserNick=a83533774; AU=F64; UN=a83533774; UE=\"543429245@qq.com\"; BT=1488174612516; access-token=ba5921ec-6063-43fa-bf22-31a6fec43a33; avh=49408103%2c17427655%2c57470073%2c54948790%2c54948790; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1487846336,1488173816,1488173847,1488174727; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1488176398; dc_tos=om0s9a; dc_session_id=1488176253802",
    'cache-control': "no-cache",
    'postman-token': "a6948124-e7b7-d13b-7b81-5b735509b765"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
print(response.text)
