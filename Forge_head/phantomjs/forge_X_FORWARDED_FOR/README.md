/***********************************
code:javascript
system:win  ||  linux
auther: luyi
mail : 543429245@qq.com
github: luyishisi
blog: https://www.urlteam.org
date：2016.10.28
逻辑说明：使用phantomjs无界面浏览器作为操作平台，破解对方针对js解析的反爬虫辨别.并且伪造多代理的假象，伪造xforword。可以多写几个值用，号隔开，模拟多代理连跳
************************************/

做一个demo而已。可以使用命令
phantomjs forge_X_FORWARDED_FOR.js http://www.stilllistener.com/checkpoint1/test11/
可以检测使用伪造的效果，你要知道真实的ip是不可以伪造的（真伪造了数据回不来，可用来DDOS），但是可以伪造出使用代理的假象。并且部分网站是只检测该项。
