import requests

url = "https://www.top1.cn/home/Reg.aspx"

querystring = {"act":"check_user_reg_small","clientid":"MobilePhoneNo","MobilePhoneNo":"13122862646","_":"1530604394256"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'referer': "https://www.top1.cn/home/Reg.aspx",
    'x-requested-with': "XMLHttpRequest",
    'cookie': "Toponecn_SessionSource=yxg8ghAqF1Azf/nAJiFknc4y8D5J24ocB5cb14WvFtE=; ASP.NET_SessionId=pk3wk2bltph5ab45cgvvfz45; Hm_lvt_428b448cd581fd591980814d20a74795=1530604393; Hm_lpvt_428b448cd581fd591980814d20a74795=1530604395; Hm_lvt_3d72e937515495dba409690920f848cf=1530604395; Hm_lpvt_3d72e937515495dba409690920f848cf=1530604395",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'postman-token': "cd0a3410-17eb-94d7-ef77-805499808fd6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
