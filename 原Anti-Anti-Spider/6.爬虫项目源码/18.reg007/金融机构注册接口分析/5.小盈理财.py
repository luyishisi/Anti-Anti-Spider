import requests

url = "https://www.xiaoying.com/user/apiCheckMobile"

querystring = {"app_ver":"2"}

payload = "mobile=17513502495&_fromAjax_=1&_csrfToken_=d41d8cd98f00b204e9800998ecf8427e"
headers = {
    'cookie': "source=10001; Hm_lvt_6a5064ae576aec13acf46a38ed77e29d=1531213525; Hm_lpvt_6a5064ae576aec13acf46a38ed77e29d=1531213530; uuid=139223000214405229; _no_report=0; captchaKey=3903205b4477af1314e",
    'origin': "https://www.xiaoying.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'x-requested-with': "XMLHttpRequest",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'cache-control': "no-cache",
    'authority': "www.xiaoying.com",
    'referer': "https://www.xiaoying.com/user/register",
    'postman-token': "9dcaef18-701b-04d3-2347-4f32d0463101"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

#  {"ret":0,"msg":"not exist"}
