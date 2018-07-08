import requests

url = "https://ac.ppdai.com/registercheck"

querystring = {"callback":"jQuery17107792932060091637_1530947578091","name":"mobilePhone","value":"17513502491","_":"1530947585656"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    'referer': "https://ac.ppdai.com/User/Register?Redirect=",
    'x-requested-with': "XMLHttpRequest",
    #'cookie': "regSourceId=0; referID=0; fromUrl=; referDate=2018-7-7%2015%3A10%3A32; gr_user_id=7a5646e2-7371-4d62-bc8f-91d68f22b27a; gr_session_id_b9598a05ad0393b9=bb6c3838-b2e9-4820-b1bf-1105bc8809ce; uniqueid=7d8fb617-7c8d-4109-ac81-28d89ce983e5; gr_session_id_b9598a05ad0393b9_bb6c3838-b2e9-4820-b1bf-1105bc8809ce=true; aliyungf_tc=AQAAAGDARE3tdQkAIxYRDg+MCc4+62qx; __tsid=200841278; __vsr=1530947435906.refSite%3Dhttps%3A//www.ppdai.com/%7Cmd%3Dreferral%7Ccn%3Dreferral; openid=f0faff5f2fd37f278591092fb253d14c; currentUrl=https%3A%2F%2Floan.ppdai.com%2Fqrcode; JSESSIONID=E8B5A30B2E07D6E579E6469413F5C91E; __fp=fp; __vid=1568200942.1530947435906; __sid=1530947435906.3.1530947578154; Hm_lvt_f87746aec9be6bea7b822885a351b00f=1530947433; Hm_lpvt_f87746aec9be6bea7b822885a351b00f=1530947578; reg_mobile_remainTime=24",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'postman-token': "a8127c3b-bb59-f6d9-c6f7-13d61bc571d5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
