##################################
#         Author:Lengyue         #
##################################
# Filename: core_web.py          #
# Use: web主程序/主入口 调用解析器 #
# Last Edit:2017/12/8 8:42       #
# Github: 736917271              #
# License: MIT                   #
##################################



from flask_cors import *
from flask import Flask
from flask import request
import requests
import json
import time
import class_ali

app = Flask(__name__)

#定义入口 /parse
@app.route('/parse')
def load():
    try:
        #获取参数
        MAXA = request.args.get("key")
        scene = request.args.get("scene","")
        sign = request.args.get("sign", "AUTO")

        start = time.time()
        retry = 0
        dp = {
            "errcode":-1
        }
        #调用主程序
        dp = class_ali.Ali().parse(MAXA, scene, sign)

        if dp["errcode"] != "0":
            #如果异常
            return json.dumps({
                "errcode": dp["errcode"],
                "msg": "No result"
            })
        else:
            dp["time"] = time.time()
            dp["cost_time"] = time.time() - start
            return json.dumps(dp)
    except:
        return json.dumps({"errcode":500})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", threaded=True)