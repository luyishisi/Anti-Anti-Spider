# -*- coding: utf-8 -*-
import scrapy


class IpSpider(scrapy.Spider):
    name = "ip"
    allowed_domains = ["www.j4.com.tw"]
    start_urls = (
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
        'http://www.j4.com.tw/james/remoip.php',
    )

    def parse(self, response):
        print response.body
        pass
