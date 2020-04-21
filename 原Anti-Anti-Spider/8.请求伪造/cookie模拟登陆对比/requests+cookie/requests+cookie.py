import requests

url = "https://www.urlteam.org/"

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'cookie': "wp-settings-1=libraryContent%3Dbrowse%26editor%3Dtinymce%26wplink%3D1%26mfold%3Do%26post_dfw%3Doff%26hidetb%3D1%26unfold%3D1%26imgsize%3Dfull%26urlbutton%3Dfile%26advImgDetails%3Dhide%26editor_plain_text_paste_warning%3D1; wp-settings-time-1=1491381046; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_5366dc8554b569ada9850cdd716c822b=luyishisi%7C1493186146%7CRBHJXsxODpVxfTxB67Zf7u3fYfM6JnvdbwxnWmA77AJ%7C823fef87172e3e1b0b351779e8260226af91f30d2a27c9b20642ac0dd3041d49; wfwaf-authcookie-444d9607ba5ef2d3e5b98f009059a039=1%7Cadministrator%7C4ac369d5a8091561ca2a0516b0552777839066011565effce7a6afa78237d956; wfvt_2173332352=58fe9e2044508; slimstat_tracking_code=46205.6a4fcfb2ee1582aeabffca18544d61d5",
    'host': "www.urlteam.org",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'x-forwarded-for': "111.202.141.60",
    'postman-token': "df69dfed-82f0-12a7-4873-2695e9323c17"
}

response = requests.request("GET", url, headers=headers)

print(response.text.encode("utf-8"))
