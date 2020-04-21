import requests

url = "http://gs.amac.org.cn/amac-infodisc/api/pof/manager"

querystring = {"rand":"0.04988045735095259","page":"0","size":"20"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"rand\"\r\n\r\n0.04988045735095259\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"size\"\r\n\r\n20\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "2",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'host': "gs.amac.org.cn",
    'origin': "http://gs.amac.org.cn",
    'pragma': "no-cache",
    'referer': "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'postman-token': "155506bb-9f5e-1324-4be4-8b0724a4d015"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
