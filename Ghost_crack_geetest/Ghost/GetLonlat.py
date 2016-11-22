#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import os
import sys
import time
import random

from ghost import Ghost

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()


def SpiderHtml(address):
    lon, lat = None, None
    ghost = Ghost()
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"
    headers = {
        'User-Agent': user_agent,
        'Referer': 'http://www.baidu.com/',
        # 'X-Forwarded-For': '114.112.133.67'
    }
    url = "http://api.map.baidu.com/lbsapi/getpoint/"
    # display=True, viewport_size=(1000, 800)
    session = ghost.start(display=False, viewport_size=(800, 600))
#    session = ghost.start(display=True, viewport_size=(800, 600))
    page, extra_resources = session.open(url, method='get', headers=headers, timeout=30)
    assert page.http_status == 200 and 'api.map.baidu.com' in page.content

    session.wait_for_page_loaded(timeout=10)
    result, resources = session.evaluate('''
            document.getElementById('localvalue').value = "%s";
            ''' % unicode(address)) 
    status, resources = session.click('.button', btn=0, expect_loading=False)
    try:
        status, resources = session.wait_for_selector(selector='#mk_0', timeout=5)
        print '1'
        status, resources = session.click('#mk_0', btn=0, expect_loading=False)
        session.wait_for_page_loaded(timeout=5)
        session.sleep(2)
        print '2'
        result, resources = session.evaluate('''document.getElementById('pointInput').value;''')
        print str(result)
        print '*'*199
        print str(resources)
        print '3'
        lonlat = str(result).split(',')
        print '5'
        lon, lat = lonlat[0], lonlat[1]
        print '6'
    except:
        print "Can't get Lonlat!!!"
    session.sleep(10)
    session.exit()
    return (lon, lat)


def main():
#    address = "世纪欢乐园"
    address = "清华大学"

    (lon, lat) = SpiderHtml(address)
    if lon is not None:
        print lon, lat


if __name__ == '__main__':

    print "The Program start time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start = time.time()
    main()
    print "The Program end time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "[%s]" % (time.time() - start)
    # raw_input("Please enter any key to exit!")
