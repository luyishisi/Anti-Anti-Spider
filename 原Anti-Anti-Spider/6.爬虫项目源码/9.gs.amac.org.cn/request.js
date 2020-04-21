/***********************************
code:javascript
system:win  ||  linux
auther: luyi
mail : 543429245@qq.com
github: luyishisi
blog: https://www.urlteam.org
date：2016.9.12
逻辑说明：使用phantomjs无界面浏览器作为操作平台，破解对方针对js解析的反爬虫辨别
************************************/
var page = require('webpage').create(),
    system = require('system'),
    address;
address = system.args[1];
 
//init and settings
page.settings.resourceTimeout = 30000 ;
page.settings.XSSAuditingEnabled = true ;
//page.viewportSize = { width: 1000, height: 1000  };
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.customHeaders = {
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",

};
page.open(address, function() {
  console.log(address);
  console.log('begin');

		});
//加载页面完毕运行
page.onLoadFinished = function(status) {
  console.log('Status: ' + status);
  console.log(page.content);
  phantom.exit();

};
