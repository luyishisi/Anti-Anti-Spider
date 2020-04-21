var system = require('system');
var args = system.args;
var url = args[1];
var page = require('webpage').create();
page.settings.resourceTimeout = 5000; // 等待5秒
page.onResourceTimeout = function(e) {
	console.log(e.errorCode);   //打印错误码
	console.log(e.errorString); // 打印错误语句
	console.log(e.url);	    //打印错误url
	phantom.exit(1);
};
page.open(url, function(status) {
	if (status === 'success') {
		var html = page.evaluate(function() {
			return document.documentElement.outerHTML;
		});
		console.log(html);
	}
	phantom.exit();
	});
//$phantomjs xx.js http://bbs.pcbaby.com.cn/topic-2149414.html
