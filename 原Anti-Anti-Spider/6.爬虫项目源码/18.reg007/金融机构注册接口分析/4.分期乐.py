

import requests

url = "https://passport.fenqile.com/register/anti_fraud_anti_register.json"

payload = "mobile=17513502496"
headers = {
    'cookie': "_SUTC=618dfbba2ad2fcf3fb0f3c04ee77a41f5e3b19aa; fs_tag=2F4B7A7AE32A09BECC0FB70E1194DABB; Hm_lvt_3592cc1c1f867054320b2773e17711c4=1531211609; Hm_lpvt_3592cc1c1f867054320b2773e17711c4=1531211609; tgw_l7_route=d9a5a79939d21eb92ffc092d933969f6; TY_SESSION_ID=943aed62-3e68-4b75-9776-dd008e7664d9; session=bkj6c7e0m4pe0ev4vmj6emom56; _fmdata=EgQ%2BJbnzf%2FdCq3jCjw8%2BZdQazlS7RlyA8tujTEXXu8Zm0p78yw8Qk2iSbxybBYwT0UIZM8%2FZIJdn8Q2YcmdtnVxHekxey%2B5VXeoeUOMK2lc%3D",
    'origin': "https://passport.fenqile.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'x-tingyun-id': "SGKPRcjfo2k;r=211716744",
    'x-requested-with': "XMLHttpRequest",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'cache-control': "no-cache",
    'authority': "passport.fenqile.com",
    'referer': "https://passport.fenqile.com/register.html?ad_tag=WWW.MAIN.HEADER.REGISTER",
    'postman-token': "8bf54840-d9cd-58da-b63b-15fb5e684fb8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

"""
接口失败，不能越过短信
{"retcode":0,"retmsg":"ok","is_anti_register":0,"anti_register_msg":"","anti_register_code":0}
{"retcode":0,"retmsg":"ok","is_anti_register":0,"anti_register_msg":"","anti_register_code":0}
"""
