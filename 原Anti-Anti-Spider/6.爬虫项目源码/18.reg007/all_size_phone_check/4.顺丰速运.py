import requests

url = "https://passport.sfbest.com/ajax/verifmobile/"

payload = "name=userMobile&param=13122864646"
headers = {
    'pragma': "no-cache",
    'origin': "https://passport.sfbest.com",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "*/*",
    'cache-control': "no-cache",
    'x-requested-with': "XMLHttpRequest",
    'cookie': "siteid=SF_CURRENT_SITE; _SF_USER_HASH_=6d101f875087fe3b; _da_a=24490488.20180703155427165066.1530604468.1530604468.1530604468.1; _da_z=24490488.1530604468.1.1.ccn=(direct)|csr=(direct)|cmd=(none); _SF_AUTH_HASH_=f9607569d10422c4; provinceid=2; cityid=52; areaid=500; townid=0; Hm_lvt_56b4bab8080250772f08703b41839413=1530514590; Hm_lpvt_56b4bab8080250772f08703b41839413=1530604486; smart_sort_flag=2; _da_b=24490488.2.10.1530604468; returnUrl=http%3A%2F%2Fwww.sfbest.com%2F; _ems_session=1417598425.33247337; _ems_visitor=1417598425.33247337; Hm_lvt_cceda50ef06cbaf44bdeaabe2470efee=1530604490; Hm_lpvt_cceda50ef06cbaf44bdeaabe2470efee=1530604490; _ga=GA1.2.328408571.1530604490; _gid=GA1.2.1903230922.1530604490; _gat=1; _sf_tj_cc=jcz3duh8c6i1530604467860.1530604468..1530604468.1.3.1530604490; _jzqa=1.3864841506510251500.1530604491.1530604491.1530604491.1; _jzqc=1; _jzqx=1.1530604491.1530604491.1.jzqsr=sfbest%2Ecom|jzqct=/.-; _jzqckmp=1; pt_s_2f9f7c43=vt=1530604490651&cad=; _jzqb=1.1.10.1530604491.1; _qzja=1.1165698840.1530604490861.1530604490861.1530604490861.1530604490861.1530604490861.0.0.0.1.1; _qzjb=1.1530604490861.1.0.0.0; _qzjc=1; _qzjto=1.1.0; pt_2f9f7c43=uid=CxesTvaRcH-Hty96phwqbg&nid=1&vid=TTyfSwc8Pp8WGW5FrO4exQ&vn=1&pvn=1&sact=1530604499696&to_flag=0&pl=6PJno4WnKt-sUAdRl1nGmw*pt*1530604490651",
    'connection': "keep-alive",
    'referer': "https://passport.sfbest.com/reg/?returnUrl=http%3A//www.sfbest.com/",
    'postman-token': "3150fc0f-104d-7b00-78bb-4a40aa6bc52d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
