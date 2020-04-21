#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from w3school.items import W3schoolItem


class W3schoolSpider(Spider):
    """爬取w3school标签"""
    #log.start("log",loglevel='INFO')
    #name为必须,需要在启动项目时制定
    name = "w3school"
    allowed_domains = ["w3school.com.cn"]
    #制定url列表,一般放置url根路口
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]

    def parse(self, response):
        #选择器获取页面源码,
        sel = Selector(response)
        #使用xparh进行筛选,选取所有div中id为navsecond的层所包含的所有div中id为course的ul中ul标签下的,li标签内容,
        sites = sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        
        #定义一个items容器
        items = []
        #site的内容包括href为链接,title为标题,
        for site in sites:
            #成为ie一个item的字典类型
            item = W3schoolItem()
            #对每一个site使用xpath抽取出a标签内的text,href,title.
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('a/@title').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            item['link'] = [l.encode('utf-8') for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            #在列表中加入这个字典
            items.append(item)

            #记录
            log.msg("Appending item...",level='INFO')


        log.msg("Append done.",level='INFO')
        return items

