var page = require('webpage').create();
    system = require('system');

// console.log(system.args[0])
// console.log(system.args[1])
// console.log(system.args[2])
address = system.args[1];

page.settings.userAgent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
page.customHeaders = {
    "X-Forwarded-For": '110.216.12.194'
};

page.viewportsize={width:2000,height:2000};

page.onResourceReceived = function(response) {
  console.log('Response (#' + response.id + ', stage "' + response.stage + '"): ' + JSON.stringify(response));
};

page.open('http://lbs.amap.com/getting-started/locate/', function() {
//page.open('http://ditu.baidu.com/', function() {
	setTimeout(function(){
	  page.render(address+'.png');
    console.log(address+'.png');
    console.log(page.content);
	  phantom.exit();
	},5000)
});
