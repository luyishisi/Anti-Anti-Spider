var page = require('webpage').create(),
    system = require('system'),
    address, output, size;

console.log('begin!');
page.viewportSize = { width: 1000, height: 1000 };
address = system.args[1];
//output = system.args[2];

page.open(address, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit(1);
    } 
    else {
        console.log('able to load the address!');
        window.setTimeout(function () {
            //page.render(output);
            page.render('jietu_6.png');
              console.log('asd')	
        }, 1000);
        window.setInterval(function () {
           // page.render(output);
            page.render('jietu_8.png');
              console.log('111asd')	
        }, 5000);
    }
});
t = 60
interval = setInterval(function(){
    if ( t > 0 ) {
        console.log(t--);
    }
    //接下来是根据不同的时间段保留不同的截图，
    if (t == 0) {
        console.log("jietu_6");
        page.render('jietu_6.png');
        //打印出页面源代码。
        console.log(page.content);
        phantom.exit();
    }
    if (t == 2) {
        console.log("jietu_5");
        page.render('jietu_5.png');
    }
    if (t == 4){
        console.log("jietu_4");
        page.render('jietu_4.png');
    }
    if (t == 5){
        console.log("jietu_3");
        page.render('jietu_3.png');
    }
    if ( t == 10 ){
      console.log("jietu——1");
      page.render('jietu_1.png');
      console.log('click_begin');
    }
}, 1000);
