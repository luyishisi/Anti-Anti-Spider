# -*- coding: utf-8 -*-

# Scrapy settings for w3school project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'w3school'

SPIDER_MODULES = ['w3school.spiders']
NEWSPIDER_MODULE = 'w3school.spiders'

ITEM_PIPELINES = {  
    'w3school.pipelines.W3SchoolPipeline':300  
}  
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'w3school (+http://www.yourdomain.com)'
