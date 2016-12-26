分布式爬虫的样例

文件一:

push_redis.py
用于制定一个num值,添加页面在:
http://www.meizitu.com/a/list_1_ num .html

到

http://www.meizitu.com/a/list_1_ num+100 .html
这一百个页面中的所有页面的图片,加入到redis队列中

文件二:

read_redis_dow_img.py
从本机读取redis队列,并且下载该队列中的图片存放到./pic
本程序可以开启任意多个.并且可以修改其中的redis设置从而实现多机器分布式的结构基础



