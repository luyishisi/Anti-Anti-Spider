import requests

url = "https://www.nonobank.com/api/common/check/mobile/18128867646"

querystring = {"noncestr":"zuoyvd4edka","timestamp":"1530964185987","signature":"a39c2b569eb04b4ab41de0a0fa7890e2","appId":"nono"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'accept': "*/*",
    'referer': "https://www.nonobank.com/Register",
    'x-requested-with': "XMLHttpRequest",
    #'cookie': "PHPSESSID=8l3anbelct9u7iva1205vc56q1; channel_am_id=352; _fmdata=EgQ%2BJbnzf%2FdCq3jCjw8%2BZdQazlS7RlyA8tujTEXXu8Zm0p78yw8Qk2iSbxybBYwTTKL9UaBVLz3VeJo%2BZd%2BIu2E%2BDH6UxirOgR0B707%2BnlE%3D",
    'connection': "keep-alive",
    'cache-control': "no-cache"
    #'postman-token': "3dff6360-1299-a38b-2b5b-5e483447a8f0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
