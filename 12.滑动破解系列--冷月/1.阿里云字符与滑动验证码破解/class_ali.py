##################################
#         Author:Lengyue         #
##################################
# Filename: class_ali.py         #
# Use: 阿里验证码识别类            #
# Last Edit:2017/12/8 8:42       #
# Github: 736917271              #
# License: MIT                   #
##################################



import requests
import time
import random
import json
import base64
import re

#定义通用UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.0.3112.113 Safari/537.36' % random.randint(50,60),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

class Ali:
    #主函数
    def parse(self,MAXA,scene,sign,_n = "099#KAFE3GEjE7EE7YTLEEEEE6twSXLMC6fFScwMn6DqzuF0hfVhSXJEG6VhSXwMnpA3ZcvUA6PhZcsIV6tFSXRFn6jhal97G6gTDuJYG6DEZXnMSwoTEEvlT1ZugUMqv35nE7EKlGYO/0ColGwTJGFETEEEbOplE7EF9mC9ujSTEELlluaL+hhuGpdTEEMFluutG/cPE7EUlllP/3iSlllllurdt37FZlllWsaStEgtlllO/3iS16allurdt37InIoTE1UEFspC/qYWcR4f9BZnnsEnbaFp3y9MPzXnqSbqPtWG6edZLMrtSAoQ6w+zE7Tx1424EHq6mrgrLL0o1DN7smyU0HU6mCXSK2mSogUp3c7CQLYDaESCQwadRh1RJJW8MlSAp7PMK2muz84ULFUvbHwgBwDRi1XdIu7QRIGRyUQl+EoTEEylEcZdt3xmE7EFlllbr25TEE7EYRpC6GFE19dI3yZmN9llHioTEEvlwq+dwYslEEdnE7EKlGiV/+UewKaS4GFETlllsyaGn049E7EFEE1CbY=="):
        print("Start -> ",MAXA,scene)
        retry = 0
        while retry < 5:
            retry += 1
            # 如果sign是AUTO模式 也就是和aliyun官方例子一样的格式 那么可以自动生成
            if sign == "AUTO":
                sign = "%s:%s:%s" % (MAXA, str(int(time.time() * 1000)), random.random())
            # 准备第一个请求包,初始化请求
            params = {
                "a": MAXA,
                "t": sign,
                "n": _n,
                "p": {},
                "scene": scene,
                "asyn": 0,
                "lang": "cn",
                "v": 849,
                "callback": "jsonp_0997604178571166"
            }
            first_response = requests.get("http://cf.aliyun.com/nocaptcha/analyze.jsonp", params=params, headers= headers).text
            
            # 利用正则提取json数据,解析
            first_json = json.loads(re.findall(r"jsonp_0997604178571166\((.*?)\);", first_response)[0])
            print(first_json)

            # 第二个包 获取验证码
            csessionid = first_json["result"]["csessionid"]
            params = {
                "identity": MAXA,
                "sessionid": csessionid,
                "token": sign,
                "style": "bak_default",
                "callback": "jsonp_0792059742153036"
            }
            second_response = requests.get("http://diablo.alibaba.com/captcha/image/get.jsonp", params=params, headers= headers).text
            print(second_response)

            # 利用正则提取json数据,解析
            second_json = json.loads(re.findall(r"jsonp_0792059742153036\((.*?)\);", second_response)[0])
            captoken = second_json["result"]["captchaToken"]
            b64_pic = second_json["result"]["data"][0]

            # 利用正则提取base64图片 转为bytes
            bts = re.findall(r"data:image/jpg;base64,(.*)", b64_pic)[0]
            retry_a = 0
            while retry_a < 5:
                try:
                    # 注意 这里是请求图像识别接口, 本代码配套了两种
                    # 一种是开箱即用的 exe 就是
                    # 
                    # ans = requests.get("http://127.0.0.1:13852/", params={
                    #     "method": "cnn",
                    #     "b64":bts
                    # }).text
                    # ans = json.loads(ans)
                    # ans = ans["cnn"]
                    # 
                    # 另一种是python cnn 需要安装tf 在这里
                    ans = requests.get("http://127.0.0.1:5000/api", params={
                        "method": "cnn",
                        "b64":bts
                    }).text
                    
                    print(ans)
                    break
                except:
                    retry_a += 1

            # 第三个包 最终请求
            checkcode = {"answer": ans, "captchaToken": captoken}
            params = {
                "csessionid": csessionid,
                "checkcode": json.dumps(checkcode),
                "a": MAXA,
                "t": sign,
                "n": _n,
                "p": '{"ksl":["' + ans + '"]}',
                "lang": "cn",
                "v": "849",
                "callback": "jsonp_0480553736024979",

            }
            third_response = requests.get("http://cf.aliyun.com/captcha/checkcode.jsonp", params=params, headers= headers).text

            # 利用正则提取json数据,解析
            third_json = json.loads(re.findall(r"jsonp_0480553736024979\((.*?)\);", third_response)[0])
            if not "result" in third_json.keys() or not "sig" in third_json["result"]:
                print("验证码错误")
                pass
            else:
                # 返回最终结果
                final_ans = {
                    'errcode':'0',
                    'csessionid': csessionid,
                    'sig': third_json["result"]["sig"],
                    'token': MAXA,
                    'scene': scene,
                    "sign": sign,
                    "retry": retry - 1
                }
                return final_ans
        # 验证始终失败
        return {"errcode":"501","msg":"UnknownErr"}