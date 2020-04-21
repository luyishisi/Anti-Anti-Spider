# -*- coding: utf-8 -*-

import requests
import requesocks
import os
url="https://www.baidu.com/"
session = requesocks.session()
session.proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}


headers = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2)"}
ipz = session.get(url,headers=headers)
ip_page = ipz.text.encode('utf-8')
print ip_page



#次数满  换ip
#os.system("""(echo authenticate '"nj_pass"'; echo signal newnym; echo quit) | nc localhost 9051""" )
