import requests

#url = "http://www.urlteam.org/"

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "www.baidu.com",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'x-forwarded-for': "111.202.141.60",
    'postman-token': "3eed460d-872d-9df2-8362-4200cbe51645"
    }

# url = "http://www.baidu.com/"
#
# response = requests.request("HEAD", url, headers=headers)
# print response.status_code
# print response.url
#
# response = requests.request("GET", url, headers=headers)
# print response.status_code
# print response.url

# url = "https://www.baidu.com/"
url = "http://www.urlteam.org/"

# response = requests.request("HEAD", url, headers=headers)
# print response.status_code
# print response.url

response = requests.request("GET", url, headers=headers)
print response.status_code
print response.url
#print(response.text.encode('utf-8'))
