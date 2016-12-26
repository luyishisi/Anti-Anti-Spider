#coding:utf-8
#mporting base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
from scrapy_redis.spiders import RedisSpider
from redis import Redis
import os
import random


class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        r = Redis(host='localhost', port=6379, db=0)
        proxy_ip = str(r.lpop("ip:port"))

        request.meta['proxy'] = proxy_ip

        proxy_user_pass = "2476371236@qq.com:luyi123"
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

        print '+'*8, 'the Current ip address is', proxy_ip, '+'*8

        #用于伪造user-agent
        try:
            useragents = []
            useragentsock = open(os.path.basename("user_agent.txt"),"r")
            for record in useragentsock:
                useragents.append(record.rstrip("\n"))
            useragentsock.close()

            useragent = random.choice(useragents)
            request.headers.setdefault('User-Agent',useragent)
        except:
            print "useragent--error"
            pass
