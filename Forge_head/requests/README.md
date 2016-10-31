请求头信息伪造

使用read_useragent_txt.py 
在随机读取user-agent文本中，我访问自己的博客，并且后nginx检查了这次访问：
信息如下：
使用的user-agent： Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; MEGAUPLOAD 2.0)

后台记录到的是：
ip地址 - - [27/Oct/2016:10:36:43 +0800] "GET / HTTP/1.1" 200 12353 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; MSN 9.0; MSNbMSNI; MSNmen-us; MSNcOTH; MPLUS)"

这还是有伪造效果的


伪造请求的referer   ip地址
同样是在header字典中设置referer选项，后台记录到的信息是：

真实ip - - [27/Oct/2016:10:46:00 +0800] "GET / HTTP/1.1" 200 12353 "123.123.123.123" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"

可以看到，伪造字段是可以非常轻松的后后台被筛选出来。但是一些网站经常会疏忽，，曾经用这个伪造字段而不是用代理ip去大量跑一个网站。

因为这个字段其实会自动产生，在使用代理的时候，如果你有用多个代理，则会形成一个ip地址串。。如代理不匿名的话就很容易检查出来。
