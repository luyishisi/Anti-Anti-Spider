#coding:utf-8

import requests
from recognise import *
from PIL import Image
import base64
import getpass


def login(username,passwd):
    session=requests.session()
    session.get('http://wsxk.hust.edu.cn/login.jsp').text
    img=session.get('http://wsxk.hust.edu.cn/randomImage.action').content
    with open('captcha.jpeg','wb') as imgfile:
        imgfile.write(img)
    imageRecognize=CaptchaRecognize()
    image=Image.open('captcha.jpeg')
    result=imageRecognize.recognise(image)
    string=''
    for item in result:
        string+=item[1]
    print(string)
    data={
    'usertype':"xs",
    'username':username,
    'password':passwd,
    'rand':string,
    'sm1':"",
    'ln':"app610.dc.hust.edu.cn"
    }
    headers = {
        'Host':"wsxk.hust.edu.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        'Referer':"http://wsxk.hust.edu.cn/login.jsp",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    session.post('http://wsxk.hust.edu.cn/hublogin.action',data=data,headers=headers)
    html=session.get('http://wsxk.hust.edu.cn/select.jsp',headers=headers).text
    print(html)
    return session

def main():
    username=input('username:')
    passwd=base64.b64encode(getpass.getpass('Passwd:').encode()).decode()
    login(username,passwd)

main()
