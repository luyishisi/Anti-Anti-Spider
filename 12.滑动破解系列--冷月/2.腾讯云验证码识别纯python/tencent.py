# tencent.py
# Author : Lengyue

#　Target: http://open.captcha.qq.com/cap_web/experience-slideJigsaw.html

import requests
import time
import random
import re
import hashlib
import os
from PIL import Image, ImageChops

class VerifyCode:
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    #js 的 CDATA
    def GetCdata(self):
        arr = self.chlg
        for i in range(int(arr['M'])):
            if hashlib.md5((arr["randstr"] + str(i)).encode()).hexdigest() == arr["ans"]:
                self.cdata = i
                return 0
        self.cdata = 0
        return 0

    # 下载图片
    def GetImg(self, index):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Referer": "https://ssl.captcha.qq.com/cap_union_new_show"
        }

        params = {
            'aid': self.aid,
            'asig': self.asig,
            'captype': '',
            'protocol': 'https',
            'clientype': '2',
            'disturblevel': '',
            'apptype': '',
            'curenv': 'open',
            'ua': '',
            'uid': '',
            'cap_cd': '',
            'height': '45',
            'lang': '2052',
            'fb': '1',
            'theme': '',
            'rnd': '83008',
            'rand': random.randint(100000,999999),
            'sess': self.sess,
            'firstvrytype': '1',
            'showtype': 'point',
            'vsig': self.vsig,
            'img_index': index
        }

        return requests.get(url= "https://captcha.guard.qcloud.com/cap_union_new_getcapbysig", headers= headers, params= params).content

    #第一个包　获取 sess
    def GetFirstPackage(self):
        params = {
            'aid': self.aid,
            'asig': self.asig,
            'captype': '',
            'protocol': 'https',
            'clientype': '2',
            'disturblevel': '',
            'apptype': '',
            'curenv': 'open',
            'ua': '',
            'uid': '',
            'cap_cd': '',
            'height': '45',
            'lang': '2052',
            'fb': '1',
            'theme': '',
            'rnd': random.randint(100000, 999999),
            'collect': '',
            'firstvrytype': '1',
            'random': random.random(),
            '_': int(time.time() * 1000)
        }

        response = requests.get("https://captcha.guard.qcloud.com/cap_union_prehandle", params= params, headers= self.headers).json()
        self.sess = response["sess"]

    # 第二个包　获取　vsig randstr inity ans
    def GetSecondPackage(self):
        params = "aid=%s&asig=%s&captype=7&protocol=https&clientype=1&disturblevel=1&apptype=&noheader=1&color=1AAD19&showtype=&fb=1&theme=&lang=2052&sess=%s&fwidth=0&uid=&cap_cd=&rnd=%s&rand=%s" % (self.aid,self.asig, self.sess, random.randint(100000,999999),random.random())
        response = requests.get("https://captcha.guard.qcloud.com/cap_union_new_getsig", params=params,
                                headers=self.headers).json()
        self.vsig = response["vsig"]
        self.inity = response["inity"]
        self.chlg = response["chlg"]

    #　第三个包　获取 _c, websig
    def GetThirdPackage(self):
        params = {
            'aid': self.aid,
            'asig': self.asig,
            'captype': '',
            'protocol': 'https',
            'clientype': '2',
            'disturblevel': '',
            'apptype': '',
            'curenv': 'open',
            'ua': '',
            'uid': '',
            'cap_cd': '',
            'height': '45',
            'lang': '2052',
            'fb': '1',
            'theme': '',
            'rnd': random.randint(100000,999999),
            'rand': random.random(),
            'sess': self.sess,
            'firstvrytype': '1',
            'showtype': 'point',

        }
        response = requests.get("https://captcha.guard.qcloud.com/cap_union_new_show", params=params,
                                headers=self.headers).text
        #print(response)
        regular = r'cdata:f,"(.*?)":w,websig:"(.*?)"'
        response = re.findall(regular, response)[0]
        self._c = response[0]
        self.websig = response[1]

    # 图片识别 采用图片异或
    def GetLocate(self):
        a = self.GetImg(0)
        b = self.GetImg(1)
        c = self.GetImg(2)
        # print(hashlib.md5(a+b+c).hexdigest())
        h = hashlib.md5(a + b + c).hexdigest()
        path = "checkcodes/" + h
        if not os.path.exists(path):
            os.makedirs(path)
        open(path + '/full.png', 'wb').write(a)
        open(path + '/a.png', 'wb').write(b)
        open(path + '/b.png', 'wb').write(c)
        img_full = Image.open(path + '/full.png')
        img_a = Image.open(path + '/a.png')
        img_diff = ImageChops.difference(img_full, img_a)

        img_diff.save(path + '/diff.png')
        pix = img_diff.load()
        result = ''
        for x in range(img_diff.size[0]):
            for y in range(img_diff.size[1]):
                (r, g, b) = pix[x, y]
                if r + g + b > 150 and y > 5 and x > 5:
                    result = str(x - 20) + "," + str(self.inity) + ";"
                    break
            if result != '':
                break
        __import__('shutil').rmtree(path)
        self.result = result

    #最终数据包
    def FinalPackage(self):
        postData = {
            'aid': self.aid,
            'asig': self.asig,
            'captype': '',
            'protocol': 'https',
            'clientype': '2',
            'disturblevel': '',
            'apptype': '',
            'curenv': 'open',
            'ua': '',
            'uid': '',
            'cap_cd': '',
            'height': '45',
            'lang': '2052',
            'fb': '1',
            'theme': '',
            'rnd': random.randint(100000,999999),
            'rand': random.random(),
            'sess': self.sess,
            'firstvrytype': '1',
            'showtype': 'point',
            'subcapclass': '10',
            'vsig': self.vsig,
            'ans': self.result,
            'cdata': self.cdata,
             self._c: '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',
            'websig': self.websig,
            'fpinfo': 'undefined',
            'tlg': '1',
            'vlg': '0_0_0',
            'vmtime': '_',
            'vmData': '',
        }
        return requests.post(url="https://captcha.guard.qcloud.com/cap_union_new_verify", data=postData, headers= self.headers
                             ).json()

    def Verify(self):
        self.GetFirstPackage()
        self.GetSecondPackage()
        self.GetThirdPackage()
        self.GetCdata()
        self.GetLocate()
        return self.FinalPackage()


    def __init__(self, aid, asig):
        self.aid = aid
        self.asig = asig

# 主入口
if __name__ == "__main__":
    aid = "1252020920"
    asig = "D48pTEFAsoRt44ABoMz3IlJUEuWQY6lNFkMNjqcQywBdCxx8ZgJTmN3Yn--MjCtap7FNG5h91-2ei18s3nswvGQTmykMuxd2rLo88fFP2c4ms5huZIk-uIW22j_1PmINp_ld3kCgKAqMUqUq9GR6kA**"
    verify_class = VerifyCode(aid,asig)
    print(verify_class.Verify())