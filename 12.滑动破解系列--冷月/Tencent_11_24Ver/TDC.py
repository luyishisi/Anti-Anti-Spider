import time
import random
import json
import math
from Crypto.Cipher import AES

from binascii import b2a_hex
import crypto
import base64

class TDC:
    def bytePad(self, text,byteAlignLen=16):    
        count = len(text)    
        mod_num=count % byteAlignLen
        if mod_num==0:        
            return text 
        add_num=byteAlignLen-mod_num
        return text+chr(add_num)*add_num
    #PTCZ 是 Cookie 的一部分 in ssl.captcha.qq.com
    #TDC_token 在 captcha.gtimg.com
    #Track轨迹 ,X,Y坐标
    def getData(self, ptcz,TDC_token,track,x,y):
        arr = {}
        token_arr = TDC_token.split(":")
        token_arr[1] = token_arr[1][:-3]
        arr["mousemove"] = []
        for i in range(random.randint(2, 4)):
            arr["mousemove"].append({"t": i, "x": random.randint(180, 190), "y": random.randint(320, 330)})
        arr["mousemove"].append({"t": i + 1, "x": random.randint(180, 190) - 40, "y": random.randint(320, 330) + 20})
        arr["mouseclick"] = []
        arr["keyvalue"] = []
        arr["user_Agent"] = "Chrome/62.0.3202.94"
        arr["resolutionx"] = 1920
        arr["resolutiony"] = 1080
        #窗口大小
        arr["winSize"] = [1230, 976]
        arr["url"] = "https://ssl.captcha.qq.com/cap_union_new_show"
        arr["refer"] = ""
        #TDC加载时间
        arr["begintime"] = int(time.time()) - 5 - random.random() * 7
        #TDC结束时间
        arr["endtime"] = int(time.time())
        #平台 1 电脑 2 手机
        arr["platform"] = 1
        arr["os"] = "other"
        arr["keyboards"] = 0
        arr["flash"] = 1
        arr["pluginNum"] = 0
        arr["index"] = 1

        arr["ptcz"] = ptcz
        arr["tokenid"] = token_arr[0]
        arr["a"] = token_arr[0]
        #不知道是啥
        arr["btokenid"] = None
        arr["tokents"] = token_arr[1]
        arr["colorDepth"] = 24
        arr["cookieEnabled"] = True
        arr["timezone"] = 8

        arr["wDelta"] = 0
        arr["keyUpCnt"] = 0
        arr["keyUpValue"] = []
        arr["ips"] = {
            "in":["192.168.1." + str(random.randint(100,200))]
        }
        arr["mouseUpValue"] = [
            {
                "t": random.randint(4,6),
                "x": random.randint(100,120),
                "y": random.randint(240,260)
            }
        ]
        arr["mouseUpCnt"] = len(arr["mouseUpValue"])
        arr["orientation"] = [
            {
                "t": 0,
                "x": 0,
                "y": 0
            }
        ]
        arr["bSimutor"] = 0
        arr["focusBlur"] = {
            "in": [],
            "out": [],
            "t": []
        },
        #Flash Version
        arr["fVersion"] = random.randint(26, 27)
        arr["charSet"] = "UTF-8"
        arr["resizeCnt"] = 0
        arr["errors"] = []
        arr["screenInfo"] = str(arr["resolutionx"]) + "-" + str(arr["resolutiony"]) + "-" + str(arr["resolutionx"] -40 ) + "-" + str(arr["colorDepth"]) + "-*-*-*"
        temp = {
            'ft': 'qf_7P_n_H',
            'clientType': '1',
            'coordinate': [
                int(math.floor(-0.00012336060251915386 * x * x + 0.73032073756655 * x - 22.674016361511526 - 38 / x)),
                int(0.4 * y + 121.6),
                float(str(376 / 680)[:6])
            ],
            'trycnt': 1,
            'refreshcnt': 0,
            'slideValue': track,
            'jshook': 1
        }

        dic = ["mousemove", "mouseclick", "keyvalue", "user_Agent", "resolutionx", "resolutiony", "url", "refer", "begintime", "endtime", "platform", "os", "keyboards", "flash", "pluginNum", "index", "ptcz", "tokenid"]
        for i in temp.keys():
            if i not in dic:
                arr[i] = temp[i]

        json_dump = json.dumps(arr)
        sbstr = "0123456789abcdef"
        temp = [0,0,0,0]
        for i in range(len(sbstr)):
            temp[i >> 2] |= ord(sbstr[i]) << 24 - 8 * (i % 4)
        okencrypt_1 = {
            "sigBytes":len(sbstr),
            "words":temp
        }
        okencrypt_2 = {
            "sigBytes": len(sbstr),
            "words": temp
        }
        wbd = json_dump
        for i in range(15 - len(wbd) % 16):
            wbd = wbd + " "
        cipher = AES.new("0123456789abcdef", AES.MODE_CBC, "0123456789abcdef")
        return base64.b64encode(cipher.encrypt(self.bytePad(wbd)))
if __name__ == "__main__":
    track = [[224,364,1],[2,0,32],[10,-2,16],[13,-2,17],[19,-3,16],[16,-1,17],[28,-2,17],[36,0,16],[34,0,17],[27,0,17],[19,4,16],[12,4,16],[2,0,18],[2,3,33],[4,3,16],[6,4,17],[6,2,17],[0,0,16],[0,0,17],[4,2,17],[1,1,17],[3,0,16],[2,0,17],[3,0,18],[3,0,16],[1,0,16],[3,0,16],[0,0,26],[0,0,144],[2,0,14],[2,0,16],[2,0,17],[2,0,23],[0,0,10],[1,0,17],[1,0,20],[2,0,25],[0,0,22],[0,0,25],[2,-1,17],[2,0,16],[0,0,8],[0,0,17],[1,0,19],[1,0,18],[2,0,13],[0,0,16],[0,0,17],[0,0,17],[1,0,17],[3,0,16],[0,0,75],[0,0,75],[0,0,75]]
    response = TDC().getData("","396194170:1499089992009",track,1,1)
    print(response)

