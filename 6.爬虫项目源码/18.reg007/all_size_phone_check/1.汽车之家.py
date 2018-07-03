import requests

url = "http://www.lashou.com/account/detect/mobile/"

payload = "mobile=11121167645"
headers = {
    'pragma': "no-cache",
    'cookie': "ThinkID=8mrndnhlu09qslfsn8kb7nij60; client_key=1530603744w9f0e66e1f05ed728c1cf2; Hm_lvt_afa862711632a5e8d816ae378e760404=1530603746; Hm_lpvt_afa862711632a5e8d816ae378e760404=1530603753; __utma=1.1438947249.1530603747.1530603747.1530603747.1; __utmb=1.4.9.1530603752542; __utmc=1; __utmz=1.1530603747.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); city_b=2419",
    'origin': "http://www.lashou.com",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'cache-control': "no-cache",
    'x-requested-with': "XMLHttpRequest",
    'proxy-connection': "keep-alive",
    'referer': "http://www.lashou.com/account/signup/?url=%2F",
    'postman-token': "62a2f17e-64d5-19aa-8413-c909af8db71a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
