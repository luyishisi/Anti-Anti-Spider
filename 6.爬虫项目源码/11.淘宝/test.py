#coding:utf-8
import requests

url = "https://s.m.taobao.com/search"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"event_submit_do_new_search_auction\"1------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"_input_charset\"utf-8------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"topSearch\"1------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"atype\"b------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"searchfrom\"1------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"action\"home:redirect_app_action------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"from\"1------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=皮裤男------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"sst\"1------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"n\"20------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"buying\"buyitnow------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"m\"api4h5------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"abtest\"27------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"wlsort\"27------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"style\"list------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"closeModues\"nav,selecthot,onesearch------WebKitFormBoundary7MA4YWxkTrZu0gWContent-Disposition: form-data; name=\"page\"1------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'accept': "application/json",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'cookie': "thw=ca; cna=mx3eEN4jylICAS9aUXroe7QT; uss=U7BF7ECyL2ASwrEOYQ44DNcPMBUz3pSobKdyq%2Byc6n8FghhgUKX%2BdwO8; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; ali_ab=171.15.132.56.1482321078252.3; uc2=wuf=http%3A%2F%2Fwww.umeng.com%2F%3Fspm%3D2013.1.1997523009.17.QKcgNw; cookie2=1c4616113d31ccff2a11ac55392b45c1; t=5e8eb89f88eaa0e6cc5ac88135841f4d; OUTFOX_SEARCH_USER_ID_NCOO=731539750.9226516; miid=423405037610384452; tkmb=e=E1DoNQOKQ8Bw4vFB6t2Z2ueEDrYVVa64gze6kOnl9rUYX8TY-NEwd6Vld1zxDwD4IfNVgZHErC7Qw2z4l0QSO7miPnyQLVs2v9hsW5EhbenF_tD4Y0_kjSP88i591npA_Qthylo3HFfXZs7UX6XuEPAd4QYtbexQJSdb3DTn-MUbi6LHOW70tnKirEH51Gw9pWV3XPEPAPgAvPM5QRELPMu0DvJ4SySS90WRxBXkWV7iC0Er_lIGgiIDeMwxoAFc-D2lLpi0SOqtD0dafC_ZEg&iv=0&et=1482556362; linezing_session=HWVtZf1l8XH0dACdMJQQDOt4_1482556828494E2ui_9; uc3=sg2=BYiIfEpsMbxtm040yzQn62r4dy8462CfLR73vjezc00%3D&nk2=&id2=&lg2=; hng=CN%7Czh-cn%7CCNY; tracknick=; mt=ci=0_0&cyk=2_1; v=0; _m_h5_tk=1d52cfb51a019fc6b3f3bcafcb88fc5a_1482910547070; _m_h5_tk_enc=37149113fb0caf06a0f086a605721964; _tb_token_=YfuOSRriSmBkwyRo5m4h; uc1=cookie14=UoW%2FX9Q1zQXCpw%3D%3D; JSESSIONID=299315B3B9143C57D3CEFD7E71B56B99; ___rl__test__cookies=1482995634939; l=AoWF82noU/G0VcAybR9piIJLFdq/Hzjl; isg=AhsbL2-dx8agsTsMpa_FVkRjqnlPnL4I5G5pIw1YqpsA7DDOkMBuQAkq9PYd",
    'pragma': "no-cache",
    'referer': "https://s.m.taobao.com/h5?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E7%9A%AE%E8%A3%A4%E7%94%B7&sst=1&n=20&buying=buyitnow",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'postman-token': "761c6c35-7ef9-7fbe-d235-859dd1ea4551"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text).encode('utf8')
