#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：read_useragent_txt_forge.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/10
#   语言：Python 2.7.x
#   操作：python read_useragent_txt_forge.py
#   功能：	爬取优酷网视频播放链接
#         读取一个随机的头部User-Agent 信息 添加到请求中此作为基础的伪造,
#
#-------------------------------------------------------------------------
import random
import re

import requests


# 发起请求,


def get_request(url, user_agent):
    '''参数引入及头信息'''
    if len(user_agent) < 10:
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
    # 此处修改头字段,
    headers = {
        'Host': "v.youku.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        'Cache-Control': 'no-cache',
        "Connection": "keep-alive",
        "User-Agent": user_agent,
        'Referer': 'http://www.youku.com/'
    }
    try:
        html = requests.get(url, headers=headers, timeout=20).text
        # print html
        return html
    except Exception, e:
        print Exception, e
        return -1

if __name__ == '__main__':
    # 此url为任意一个具有某视频播放窗口的页面
    url = "http://v.youku.com/v_show/id_XMTgzNDI0MjkzNg==.html?from=y1.3-movie-grid-1095-9921.86985-107667.1-1&spm=a2hmv.20009921.yk-slide-107667.5~5~5~5!2~A#paction"

    # 导入数据集并随机获取一个User-Agent
    user_agent_list = []
    f = open('user_agent.txt', 'r')
    for date_line in f:
        user_agent_list.append(date_line.replace('\r\n', ''))
    user_agent = random.choice(user_agent_list)

    # 发起请求
    html_body = get_request(url, user_agent)
    print re.findall('http://player.youku.com/player.php/sid/[A-Za-z0-9=]*/v.swf', html_body)


#-------------------测试结果-------------------------------
# 将此链接放在浏览器中可以直接播放,虽然有广告....至于别的数据太简单那就不抓了.
#[
# u'http://player.youku.com/player.php/sid/XMTgzNDI0MjkzNg==/v.swf',
# u'http://player.youku.com/player.php/sid/XMTgzNDI0MjkzNg==/v.swf'
#]
