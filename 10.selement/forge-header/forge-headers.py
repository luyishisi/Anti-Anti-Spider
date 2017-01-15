from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
dcap["phantomjs.page.customHeaders"] = {
    "X-Forwarded-For":'110.216.12.194'
}

#page.driver.headers

print 'begin'
driver = webdriver.PhantomJS(desired_capabilities=dcap)

#driver.get("https://www.baidu.com/s?wd=ip")
driver.get("https://httpbin.org/get?show_env=1")
#driver.get("http://lbs.amap.com/getting-started/locate/")

time.sleep(5)
driver.get_screenshot_as_file('01.png')
print 'end'

driver.quit()
