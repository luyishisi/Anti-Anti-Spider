![Crack Geetest](./crack-geetest.gif)

## 接口调用


```
	from basicgeetestcrack import IndustryAndCommerceGeetestCrack
    c = IndustryAndCommerceGeetestCrack(
        url="http://211.141.74.198:8083/", 
        search_text=u"工业大学",
        input_id="txtSearch",
        search_element_id="btnSearch",
        gt_element_class_name="gt_box",
        gt_slider_knob_name="gt_slider_knob",
        result_numbers_xpath='/html/body/div[1]/div[3]/div[1]/span[2]',
        result_list_verify_class='m-searchresult')
    print c.crack()
    
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
    return 搜索结果列表，cookies ： 结果列表的网页源代码已经返回，破解成功了
    return 0,None: 搜索企业的结果为0
    return None, None: 破解过程出错了，需要检查参数是否正确
    """
```

## 环境
- python>=2.7, 暂时没有支持python3.x
- selenium>=2.53.6
- `phantomjs>=2.1.1` 这点非常非常重要

## 说明
-  macos centos windows unbuntu 下分别均测试合格(需要下载对应系统的phantomjs, [chrome])
-  basicgeetestcrack默认使用phantomjs，可以更改代码使用chrome(需要下载对应的二进制工具包chrome放在目录/usr/local/bin/ 目录下)

## 特点
-  模块目前能够应用工商升级的省份，其中贵州，甘肃略有所不同，暂时不适用（需要更改）。其中吉林，西藏两省被怪物吃的情况较多
-  模块目前的滑动轨迹是一系列随机距离+较正随机距离，能够适用大部分省份的破解
-  模块支持检测滑动距离太短时(计算可能不准确),自动刷新重新截图破解(最多5次)
-  模块支持破解失败或者被怪物吃了之后，进行重新破解(最多5次)

## 破解主要思路
1. 进入对应省份搜索页面，并等待输入框与搜索按钮加载完成
2. 填入搜索企业，点击按钮，等待滑块元素加载完成
3. 截图，拖动，再截图
4. 计算需要滑动的距离
5. 生成滑动轨迹，并进行模拟滑动
6. 检测验证结果，如不成功，点击刷新按钮重新从3开始


## 需要注意的点

1. 等待元素出现不要使用sleep,有wait显示隐示等待，再等待出现之后，最后最好再等待1，2秒（我在这里坑过）参考selenium文档
2. 使用self.driver.maximize_window() 可以避免各浏览器的像素偏差
3. 滑块轨迹比较难，使用phantomjs调用move_to_element_with_offset之后，还需要click_and_hold，否则不会成功拖动（大坑）
4. 在拖动的时候，除了x的坐标需要移动，y的值也要有变动，不然会被怪物吃掉
5. 直接调用 drag_and_drop_by_offset 也会被怪物吃掉
4. 两张截图可以使用 StringIO 做为保存，省去了保存了文件图片到本地

## 需要完善的地方
1. 生成更准确性的滑块运动轨迹（考虑机器学习）
