#!/usr/bin/env python
# coding:utf8

import sys
import time
import uuid
import math
import random
import StringIO
import traceback
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

reload(sys)
sys.setdefaultencoding('utf-8')


class IndustryAndCommerceGeetestCrack(): 

    def __init__(self,
                 url,
                 search_text,
                 input_id='searchText',
                 search_element_id='u85',
                 gt_element_class_name='gt_box',
                 gt_slider_knob_name='gt_slider_knob',
                 result_numbers_xpath='//*[@id="searchtipsu1"]/p/span[2]',
                 result_list_verify_id=None,
                 result_list_verify_class=None,
                 is_gap_every_broad=True):

        """
        url: 主页面的地址
        search_text: 搜索企业名称
        input_id: 输入框网页元素id
        search_element_id: 查询按钮网页元素id
        gt_element_class_name: 滑块验证码图片元素的class类名，基本一样，在调用时可以不传参
        gt_slider_knob_name: 滑块验证码图片拖动元素的class类名，基本一样，在调用时可以不传参
        result_numbers_xpath: 用于确认是否搜索成功的 搜索结果数量的xpath,如本次搜索共`50`条结果，用时多少秒
        result_list_verify_id: 搜索结果列表一项的某个标签id值，用于确认搜索列表已经加载完成(某些网站使用ajax) or
        result_list_verify_class: 搜索结果列表一项的某个标签class类名，用于确认搜索列表已经加载完成(某些网站使用ajax)
        is_gap_every_broad: 现在已经确定为True值，是为了兼容湖北等省原先滑块小的问题，现在网站已经更改，调用时可以忽略此参数了
        """
        self.url = url
        self.search_text = search_text
        self.input_id = input_id
        self.search_element_id = search_element_id
        self.gt_element_class_name = gt_element_class_name
        self.gt_slider_knob_name = gt_slider_knob_name
        self.result_numbers_xpath = result_numbers_xpath
        self.result_list_verify_id = result_list_verify_id
        self.result_list_verify_class = result_list_verify_class
        self.is_gap_every_broad = is_gap_every_broad
        
        
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
        )

        self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
        # self.driver = webdriver.Chrome()
        
        self.driver.maximize_window()
        time.sleep(random.uniform(2.0, 3.0))

    def get_search_page(self,
                        url="http://gsxt.hljaic.gov.cn/index.jspx",
                        search_text=u"中国移动",
                        input_id=u"searchText",
                        search_element_id='u85',
                        gt_element_class_name="gt_box"):

        """点击查询按钮
            :search_text: Unicode, 要输入的文本
            :input_id: 输入框网页元素id
            :search_element_id: 查询按钮网页元素id
            :gt_element_class_name: 验证码图片网页元素class名
        """
        # 根据页面进入主页面，并等待搜索框id出现
        print 'url: ', url
        self.driver.get(url)
        
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((By.ID, input_id)))
        time.sleep(random.uniform(2.0, 3.0))
       
        # 清空搜索框，搜索企业，点击搜索
        element.clear()
        element.send_keys(search_text)
        element = self.driver.find_element_by_id(search_element_id)
        element.click()
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            gt_element_class_name)))
        time.sleep(random.uniform(2.0, 3.0))
        print 'element: ', element.text

    def crop_captcha_image(self, gt_element_class_name="gt_box"):

        """截取验证码图片

        :gt_element_class_name: 验证码图片网页元素id
        :returns: StringIO, 图片内容

        """
        captcha_el = self.driver.find_element_by_class_name(
            gt_element_class_name)
        location = captcha_el.location
        size = captcha_el.size
        left = int(location['x'])
        top = int(location['y'])
        right = int(location['x'] + size['width'])
        bottom = int(location['y'] + size['height'])

        screenshot = self.driver.get_screenshot_as_png()
        print left, top, right, bottom
        screenshot = Image.open(StringIO.StringIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        # captcha.save("/Users/haijunt/%s.png" % uuid.uuid4().get_hex())
        return captcha

    # 点击刷新滑块验证码
    def click_refresh(self, sleep_time=0.6):
        element = self.driver.find_element_by_class_name('gt_refresh_button')
        element.click()
        time.sleep(sleep_time)

    def is_pixel_equal(self, img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0]) < 80) and (abs(pix1[1] - pix2[1]) < 80) and (
                    abs(pix1[2] - pix2[2]) < 80):
            return True
        else:
            return False

    def calculate_slider_offset(self,
                                slide_times = 0,
                                max_slide_times = 5, 
                                gt_element_class_name="gt_box", 
                                is_gap_every_broad=True):

        """计算滑块偏移位置，必须在点击查询按钮之后调用
        :slide_times: 当前滑块滑行的次数
        :max_slide_times: 滑行的最大次数
        :gt_element_class_name: 滑块元素的类名
        :is_gap_every_broad: 滑块的元素是不是非常少，原先湖北等几个省有这样情况，现在无
        :returns: Number
        """
        img1 = self.crop_captcha_image(
            gt_element_class_name=gt_element_class_name)
        self.drag_and_drop_test(x_offset=5)
        img2 = self.crop_captcha_image(
            gt_element_class_name=gt_element_class_name)
        w1, h1 = img1.size
        w2, h2 = img2.size
        if w1 != w2 or h1 != h2:
            return False
        left = 0
        flag = False
        if is_gap_every_broad:
            x_start, distance_one, distance_two = 61, 18, 8
        else:
            x_start, distance_one, distance_two = 45, 2, 0
        for i in xrange(x_start, w1):
            for j in xrange(h1):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    flag = True
                    break
            if flag:
                break
        # 如果位置太近，选择点击刷新，重新破解
        if left == x_start and slide_times < max_slide_times:
            self.click_refresh()
            return self.calculate_slider_offset(slide_times=slide_times + 1,
                                                max_slide_times=max_slide_times,
                                                gt_element_class_name=gt_element_class_name,
                                                is_gap_every_broad=is_gap_every_broad)
        elif left == x_start and slide_times >= max_slide_times:
            left = left - distance_one

        else:
            left = left - distance_two
        print u"需要划动的像素点：", left
        return left

    def drag_and_drop_test(self,
                           x_offset=0,
                           y_offset=0,
                           element_class="gt_slider_knob"):
        
        """拖拽滑块

        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :element_class: 滑块网页元素CSS类名
        :use for: 拖拽滑块出现需要滑动的位置
        """
        dragger = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(dragger, x_offset, y_offset).perform()
        time.sleep(2.8)

    def get_trail_array(self, distance):
        """
        :distance: 需要划动的像素点
        :return :array_trail,[(x,y,t)] 由x,y,及休息时间t组成的元组构成的列表
        """
        array_trail = []
        array_x = [1.0/3, 1.0/4, 1.0/5, 2.0/5, 1.0/6, 2.0/7, 3.0/8, 2.0/9]
        array_y = [-0.1, -0.2, -0.3, -0.4, -0.5, 0.1, 0.2, 0.3, 0.4, 0.5]
        last_move_distance = random.choice([-3, +3, -4, +4, -5, +5, -6, +6])
        distance = distance + last_move_distance

        x = math.ceil(distance * random.choice(array_x))
        y = random.choice(array_y)
        t = random.randint(3, 10)/100.0
        while distance - x >= 0:
            print x, y, t
            array_trail.append((x, y, t))
            distance = distance - x
            if distance == 0:
                break
            x = math.ceil(distance * random.choice(array_x))
            y = random.choice(array_y)
            t = random.randint(3, 10)/100.0

        x = 1 if last_move_distance < 0 else -1
        last_move_distance = abs(last_move_distance)
        for _ in range(last_move_distance):
            y = random.choice(array_y)
            t = random.randint(8, 20)/100.0
            array_trail.append((x, y, t))

        return array_trail

    def drag_and_drop(self,
                      x_offset=0,
                      y_offset=0,
                      gt_slider_knob_name="gt_slider_knob",
                      result_numbers_xpath='//*[@id="searchtipsu1"]/p/span[2]',
                      result_list_verify_id=None,
                      result_list_verify_class=None):
        """拖拽滑块

        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :gt_slider_knob_name: 滑块网页元素CSS类名
        :result_numbers_xpath: 搜索结果数量的xpath，有些省份如贵州可能不需要
        :result_list_verify_id: 确认有搜索结果元素出现的id or
        :result_list_verify_class: 确认有搜索结果元素的class 二选一
        :Returns: crack_result
        :return 0: 搜索结果为0(搜索的企业不存在)
        :return -1: 滑动位置失败或者被怪物吃了(有机器学习反爬),但会自动进行点击刷新重新破解(最多5次)
        :return 1: 破解成功
        """

        array_trail = self.get_trail_array(x_offset)
        for x, y, t in array_trail:
            print x, y, t

        element = self.driver.find_element_by_class_name(gt_slider_knob_name)
        ActionChains(self.driver).click_and_hold(on_element=element).perform()
        for x, y, t in array_trail:
            ActionChains(self.driver).move_to_element_with_offset(
                to_element=element, 
                xoffset=x+22,
                yoffset=y+22).perform()
            # 这个动作在phantomjs里一定需要，否则 x 是不会移动的，phantomjs成败在此一举(chrome等忽略)
            ActionChains(self.driver).click_and_hold().perform()
            # 可以在调试的时候查看 x 是否有移动，这一点非常重要
            # temp_element = self.driver.find_element_by_class_name(gt_slider_knob_name)
            # print temp_element.location
            time.sleep(t)

        time.sleep(0.4)
        print u'稍等一会儿，搜索结果马上出来...'
        ActionChains(self.driver).release(on_element=element).perform()

        time.sleep(0.5)
        element = self.driver.find_element_by_class_name('gt_info_text')
        status = element.text
        print u"破解验证码的结果: ", status
        # 这个延时必须有，在滑动后等待回复原状
        if not status:
            self.click_refresh()
            return -1
        if status.find(u'失败') > -1:
            self.click_refresh()
            return -1
        if status.find(u'怪物') > -1:
            self.click_refresh(3.4)
            return -1
        wait = WebDriverWait(self.driver, 40, 1.0)
        element = wait.until(
            EC.presence_of_element_located((
                By.XPATH, result_numbers_xpath)))
        time.sleep(random.uniform(3.0, 4.0))
        number = element.text
        print u'搜索结果数量: ', number
        if int(number) == 0:
            return 0
        else:
            wait = WebDriverWait(self.driver, 40, 1.0)
            if result_list_verify_class:
                element = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, result_list_verify_class)))
            elif result_list_verify_id:
                element = wait.until(
                    EC.presence_of_element_located((By.ID, result_list_verify_id)))
            time.sleep(random.uniform(2.0, 3.0))
            return 1

    def crack(self, max_crack_times=5):
        """
        max_crack_times: 最大点击刷新的数量
        Returns: 搜索结果列表的网页源代码，访问的cookies
        content == 0: 搜索结果为0(企业不存在)
        content == -1: 在破解过程中出错了，可以传参数不对，可能本身出错
        else source code
        """
        content = None
        cookies = None
        try:
            self.get_search_page(
                url=self.url,
                search_text=self.search_text,
                input_id=self.input_id,
                search_element_id=self.search_element_id,
                gt_element_class_name=self.gt_element_class_name)
            count = 0
            while count < max_crack_times:
                count += 1
                x_offset = self.calculate_slider_offset(
                    slide_times=0,
                    max_slide_times=5,
                    gt_element_class_name=self.gt_element_class_name,
                    is_gap_every_broad=self.is_gap_every_broad)
                status = self.drag_and_drop(
                    x_offset=x_offset,
                    gt_slider_knob_name=self.gt_slider_knob_name,
                    result_numbers_xpath=self.result_numbers_xpath,
                    result_list_verify_id=self.result_list_verify_id,
                    result_list_verify_class=self.result_list_verify_class)
                if status == 1 or status == 0:
                    break
            else:
                print u'验证码破解已经达到最大次数: %s' % max_crack_times

            if status == 0:
                content, cookies = 0, None
            elif status == -1:
                content, cookies = None, None
            else:
                content, cookies = self.driver.page_source, self.driver.get_cookies()
        except:
            print self.driver.page_source
            print traceback.print_exc()
        finally:
            self.driver.quit()
        return content, cookies


if __name__ == '__main__':
    # # 湖北
    # c = IndustryAndCommerceGeetestCrack(
    #     url="http://xyjg.egs.gov.cn/ECPS_HB/index.jspx", 
    #     search_text=u"工业大学",
    #     result_list_verify_id='gggscpnamebox')
    # print c.crack()[1]

    # 吉林
    c = IndustryAndCommerceGeetestCrack(
        url="http://211.141.74.198:8083/", 
        search_text=u"工业大学",
        input_id="txtSearch",
        search_element_id="btnSearch",
        gt_element_class_name="gt_box",
        gt_slider_knob_name="gt_slider_knob",
        result_numbers_xpath='/html/body/div[1]/div[3]/div[1]/span[2]',
        result_list_verify_class='m-searchresult')
    print c.crack(3)[1]

    # # 陕西
    # c = IndustryAndCommerceGeetestCrack(
    #     url="http://xygs.snaic.gov.cn/ztxy.do?method=index&random=1479870596271", 
    #     search_text=u"工业大学",
    #     input_id="entname",
    #     search_element_id="popup-submit",
    #     gt_element_class_name="gt_box",
    #     gt_slider_knob_name="gt_slider_knob",
    #     result_numbers_xpath='//*[@id="myDiv"]/p/span',
    #     result_list_verify_class='result_item')
    # print c.crack()[1]

    # # 广西
    # c = IndustryAndCommerceGeetestCrack(
    #     url="http://www.gxqyxygs.gov.cn/sydq/loginSydqAction!sydq.dhtml", 
    #     search_text=u"工业大学",
    #     input_id="keyword_qycx",
    #     search_element_id="popup-submit",
    #     gt_element_class_name="gt_box",
    #     gt_slider_knob_name="gt_slider_knob",
    #     result_numbers_xpath='/html/body/div[5]/p/span',
    #     result_list_verify_class='title')
    # print c.crack()[1]

    # # 河北
    # c = IndustryAndCommerceGeetestCrack(
    #     url="http://www.hebscztxyxx.gov.cn/notice/", 
    #     search_text=u"工业大学",
    #     input_id="keyword",
    #     search_element_id="buttonSearch",
    #     gt_element_class_name="gt_box",
    #     gt_slider_knob_name="gt_slider_knob",
    #     result_numbers_xpath='//*[@id="wrap1366"]/div[3]/div/div/p/span',
    #     result_list_verify_class='tableContent')
    # print c.crack()[1]

    # # 云南
    # c = IndustryAndCommerceGeetestCrack(
    #     url="http://gsxt.ynaic.gov.cn/notice/", 
    #     search_text=u"工业大学",
    #     input_id="keyword",
    #     search_element_id="buttonSearch",
    #     gt_element_class_name="gt_box",
    #     gt_slider_knob_name="gt_slider_knob",
    #     result_numbers_xpath='//*[@id="wrap1366"]/div[3]/div/div/p/span',
    #     result_list_verify_class='tableContent')
    # print c.crack()[1]

    # # 青海
    # c = IndustryAndCommerceGeetestCrack(
    #     url='http://218.95.241.36/index.jspx',
    #     search_text=u'中国移动',
    #     input_id='searchText',
    #     search_element_id='click',
    #     gt_element_class_name='gt_box',
    #     gt_slider_knob_name='gt_slider_knob',
    #     result_numbers_xpath='//*[@id="searchtipsu1"]/p/span[2]',
    #     result_list_verify_id='gggscpnametext',
    #     result_list_verify_class=None,
    #     is_gap_every_broad=True)
    # content, cookies = c.crack()
    # print cookies

