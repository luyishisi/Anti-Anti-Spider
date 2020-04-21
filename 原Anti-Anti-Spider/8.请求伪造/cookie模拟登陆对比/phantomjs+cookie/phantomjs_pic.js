var page = require('webpage').create(),
    system = require('system'),
    address, output, size;

//phantom.addCookie({
//'name': '',
//'value': '',
//'domain': ''
//});
page.settings.resourceTimeout = 30000 ;
page.settings.XSSAuditingEnabled = true ;
//page.viewportSize = { width: 1000, height: 1000  };
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36';
page.customHeaders = {
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Cookie": "wp-settings-1=libraryContent%3Dbrowse%26editor%3Dtinymce%26wplink%3D1%26mfold%3Do%26post_dfw%3Doff%26hidetb%3D1%26unfold%3D1%26imgsize%3Dfull%26urlbutton%3Dfile%26advImgDetails%3Dhide%26editor_plain_text_paste_warning%3D1; wp-settings-time-1=1491381046; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_5366dc8554b569ada9850cdd716c822b=luyishisi%7C1493186146%7CRBHJXsxODpVxfTxB67Zf7u3fYfM6JnvdbwxnWmA77AJ%7C823fef87172e3e1b0b351779e8260226af91f30d2a27c9b20642ac0dd3041d49; wfwaf-authcookie-444d9607ba5ef2d3e5b98f009059a039=1%7Cadministrator%7C4ac369d5a8091561ca2a0516b0552777839066011565effce7a6afa78237d956; wfvt_2173332352=58fe9e2044508; slimstat_tracking_code=46205.6a4fcfb2ee1582aeabffca18544d61d5",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
};
if (system.args.length < 3 || system.args.length > 5) {
    console.log('Usage: rasterize.js URL filename [paperwidth*paperheight|paperformat] [zoom]');
    console.log('  paper (pdf output) examples: "5in*7.5in", "10cm*20cm", "A4", "Letter"');
    console.log('  image (png/jpg output) examples: "1920px" entire page, window width 1920px');
    console.log('                                   "800px*600px" window, clipped to 800x600');
    phantom.exit(1);
} else {
    address = system.args[1];
    output = system.args[2];
    //page.viewportSize = { width: 1000, height: 1000 };
    if (system.args.length > 3 && system.args[2].substr(-4) === ".pdf") {
        size = system.args[3].split('*');
        page.paperSize = size.length === 2 ? {
            width: size[0],
            height: size[1],
            margin: '0px'
        } : {
            format: system.args[3],
            orientation: 'portrait',
            margin: '1cm'
        };
    } else if (system.args.length > 3 && system.args[3].substr(-2) === "px") {
        size = system.args[3].split('*');
        if (size.length === 2) {
            pageWidth = parseInt(size[0], 10);
            pageHeight = parseInt(size[1], 10);
            page.viewportSize = {
                width: pageWidth,
                height: pageHeight
            };
            page.clipRect = {
                top: 0,
                left: 0,
                width: pageWidth,
                height: pageHeight
            };
        } else {
            console.log("size:", system.args[3]);
            pageWidth = parseInt(system.args[3], 10);
            pageHeight = parseInt(pageWidth * 3 / 4, 10); // it's as good an assumption as any
            console.log("pageHeight:", pageHeight);
            page.viewportSize = {
                width: pageWidth,
                height: pageHeight
            };
        }
    }
    if (system.args.length > 4) {
        page.zoomFactor = system.args[4];
    }
    page.open(address, function(status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
            phantom.exit(1);
        } else {
            console.log('able to load the address!');
            window.setTimeout(function() {
                page.render(output);
                page.render('jietu_6.png');
                //                phantom.exit();
                console.log('asd')
            }, 1000);
            window.setInterval(function() {
                page.render(output);
                page.render('jietu_8.png');
                //                phantom.exit();
                console.log('111asd')
            }, 5000);
        }
    });
}
t = 27
interval = setInterval(function() {
    if (t > 0) {
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
    if (t == 4) {
        console.log("jietu_4");
        page.render('jietu_4.png');
    }
    if (t == 5) {
        console.log("jietu_3");
        page.render('jietu_3.png');
    }

    if (t == 10) {
        console.log("jietu——1");
        page.render('jietu_1.png');
        console.log('click_begin');
    }
}, 1000);
