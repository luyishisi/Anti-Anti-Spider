# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'
#载入ImageDownLoadPipeline类
#为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置
#分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，
TEM_PIPELINES = {
    'meizitu.pipelines.ImageDownloadPipeline': 300,
}
#图片储存
IMAGES_STORE = './'
#IMAGES_STORE = '/home/'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizitu (+http://www.yourdomain.com)'
