# coding:utf-8
import sys

import requests

# 中文编码设置
reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()
url = "http://baike.baidu.com/wikitag/api/getlemmas"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"limit\"\r\n\r\n30\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"timeout\"\r\n\r\n3000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"filterTags\"\r\n\r\n[0,0,0,0,0,0,0]\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tagId\"\r\n\r\n60829\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"fromLemma\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"contentLength\"\r\n\r\n40\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "116",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cookie': "BAIDUID=78FF28E42F6B7EEF8B80E7FC66AD66D6:FG=1; BIDUPSID=78FF28E42F6B7EEF8B80E7FC66AD66D6; PSTM=1482071627; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02321312299; BDUSS=EU3b01URTJmSlRPMzEydXVpUEJWcURBMjR0R2tjbjhLV2w0d3NtdkFtMlVlWDlZSVFBQUFBJCQAAAAAAAAAAAEAAABXvF4WYTgzNTMzNzc0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJTsV1iU7FdYc; BDSFRCVID=R-8sJeCCxG36inTiVQzO0Dd3tIweuWgL9Fsp3J; H_BDCLCKID_SF=tRk8oIDatKvbfP0kb-r_bn0_hM4X5-RLfar8a-OF5lOTJh0RQPnmXPFebUoRBbbw0jcv-hcnJnnzhnRdWjbke65WeaDHt6tsKKJ03bk8KRREJt5kq4bohjPXDqoeBtQm05bxoh37tPoEVnAw04nn5x4V5bPLBt3B3g5GKK8bWDF5MIDGj50WenLHMfnXetJQ2C7WsJceHJOoDDvwDMr5y4LdLp7xJMbaBmO0bMOa2q6RMJR9-Pc05xAb04oR5b0eWJLfoKtbJC05bP365ITS-t-e5eT22-usJDcrQhcH0hOWsIOjQfRcMqtZWG0LexQb-eTGsRoYWM5O8ho1DUC0Djb-jHAqJTtsb5vfstjsMC8-h5rnhPF3W6KFKP6-35KHa6rpobkb2xOSVbv2QPr0yh3LDM7AJh37JD6p5qvyJK8bElvF0TJV-JkOh-oxJpOhMnbMopvaKfQFoMJvbURvL4Lg3-7XJh8EJRAjoK-XJDv8fJ6xq4vhh4oHjHAX5-RLfauLVPOF5lOTJh0Rj4r_3-FZ0q69JU3bt5nALb5aQb3dbqQRK5bke4tX-NFetj8Jtf5; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; H_PS_PSSID=1467_21125_20697_21553_21670",
    'host': "baike.baidu.com",
    'origin': "http://baike.baidu.com",
    'pragma': "no-cache",
    'referer': "http://baike.baidu.com/wikitag/taglist?tagId=60829",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'postman-token': "36f249ee-4f92-4669-7491-274692665478"
}
print 'a = ['
for i in range(84):
    payload_now = payload % i
    response = requests.request("POST", url, data=payload_now, headers=headers)
    dic = eval(response.content.decode('utf8').encode('utf8'))
    dic1 = dic['lemmaList']
    for i in dic1:
        # print i['lemmaTitle'].decode('utf8').encode('utf8')
        print '"' + i['lemmaUrl'] + '",'
print ']'
