import requests
import random

proxies = "http://H5HL3E2859R0XPBD:06DF369DBC896B72@http-dyn.abuyun.com:9020"
proxies = {
    "https":proxies,
    "http":proxies
}
proxies = None
mb = "13149336649"
print(mb)

s = requests.session()
s.proxies = proxies
s.headers.update({
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'X-WECHAT-UIN': 'MTAwNTkxMzUyMA==',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; vivo y27 Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN',
})
regid = "3_10337296123414075600"

cookies = {
    "wxsrcruse":"9oXfJOJ2gZUfr2B0tcm%2BaxNqvIupMNOpROxEtdUSz514d7A8%2FYES1JVc2dSFtNeGGhbQZmhHD%2B91%2FOZdYIl1qA%3D%3D",
    "wxsrcrusehash":"MTAwNTkxMzUyMA%3D%3D",
    "pgv_pvi":"1651939328",
    "pgv_si":"s758702080"
}
for i in cookies.keys():
    s.cookies.set(i, cookies[i], domain = "weixin110.qq.com")


response = s.get("https://weixin110.qq.com/security/regverify?t=signup_verify/w_intro&regcc=86&regmobile="+mb+"&regid="+regid+"&scene=get_reg_verify_code&wechat_real_lang=zh_CN&step=start")
print(response.text)

parse = requests.get("http://192.168.121.1:8100/parse").json()
params = {
    'wechat_real_lang': 'zh_CN',
    't': 'signup_verify/w_tcaptcha_ret',
    'ret': '0',
    'ticket': parse["ticket"],
    'randstr': parse["randstr"],
    'step': 'imgcode',

}

s.headers.update({
    'Referer': 'https://weixin110.qq.com/security/readtemplate?wechat_real_lang=zh_CN&t=signup_verify/w_tcaptcha_ret&ret=0&ticket='+params["ticket"]+'&randstr='+params["randstr"]
})


print(s.get("https://weixin110.qq.com/security/regverify", params= params,verify=False).text)
