import requests

url = "https://passport.meituan.com/account/signupcheck"

payload = "mobile=18128867646"
headers = {
    'cookie': "_lxsdk_cuid=160bae30ab6c8-0f7514db17ca99-474a0521-1fa400-160bae30ab6c8; ci=30; __mta=146577035.1514963931641.1515031989914.1515035272085.6; __utma=211559370.1593181176.1514963932.1514971361.1515035272.4; __utmz=211559370.1514963932.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=211559370.|1=city=sz=1^3=dealtype=9=1; uuid=cac895be8ffc2303e67b.1514963930.0.0.0; oc=GRE_EZZSHG0WFkeWwi9FbuWR21uVTZ4qQxlyzadZqNGEz2mTGT6mkdBK2No22RM8cvS7okUF6xqrZZ56mDnfibmllkwXhJkEwIL8FAFnCq8OAXVhjXFSp-tOpReck2PxxqI_Y-9KibG0AOH4x_UrfZXR2ztyAUvxX4xCUyXy5Hc; rvd=46937542%2C44110144%2C48604516; _lxsdk_s=1645f29ddb6-853-0ac-cc7%7C%7C2; SERV=www; LREF=aHR0cDovL3d3dy5tZWl0dWFuLmNvbS9hY2NvdW50L3NldHRva2VuP2NvbnRpbnVlPWh0dHAlM0ElMkYlMkZzei5tZWl0dWFuLmNvbSUyRg%3D%3D; passport.sid=dN2PvzZcHzwkJK09hdDRHjssSfy4JB7k; passport.sid.sig=6bKKdz0JQHdkpK9Oem9ZOjOWZKo; __mta=146577035.1514963931641.1515035272085.1530604951399.7",
    'origin': "https://passport.meituan.com",
    'accept-encoding': "gzip, deflate, br",
    'x-csrf-token': "yAZS5dVI-Eyj9A8DBN88FIuJ_XNEa1OROkd4",
    'accept-language': "zh-CN,zh;q=0.8",
    'x-requested-with': "XMLHttpRequest",
    'connection': "keep-alive",
    'x-client': "javascript",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "*/*",
    'cache-control': "no-cache",
    'referer': "https://passport.meituan.com/account/unitivesignup?service=www&continue=http%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttp%253A%252F%252Fsz.meituan.com%252F",
    'postman-token': "543efcd5-b037-f637-f61c-dbeb43c5f11d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
