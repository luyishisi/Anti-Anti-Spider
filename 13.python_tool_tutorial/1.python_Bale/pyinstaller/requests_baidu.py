import requests

url = "https://www.baidu.com/"

querystring = {"tn":"92083438_hao_pg"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'postman-token': "3e51e866-3614-05e8-c3c9-813ccaa739f3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open("baidu.html","wb") as f:
    f.write(response.content)
print(response.text)
