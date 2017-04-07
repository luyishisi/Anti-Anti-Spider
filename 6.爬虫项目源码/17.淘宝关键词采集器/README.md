1：淘宝搜索程序

Search.py

功能。给定关键词与排序方式将采集到的数据存入指定文件夹内。

命令 python Search.py 关键词 文件夹 排序方式  最大页码 （价格区间）

说明：

关键词可为：皮裤 毛衣 任意名词均可 但不可包含空格

文件夹 ：将在当前目录下自动生成一个文件夹目录，包含pic文件（商品主图）待采集完成将出现一个excel文件

排序方式：有1、2、3三种选项。1为综合排序呢，2为销量排序。3为价格区间搜索，选择3的时候需要在补充两个参数作为价格区间。

使用样例：

python Search.py 皮裤 piku1 1 5   #综合排序 # 5页

python Search.py 皮裤 piku2 2 5   #销量排序

python Search.py 皮裤 piku3 3 5 100 300  #指定价格搜索


程序回头再发，持续关注。

github：淘宝关键词采集器  https://github.com/luyishisi/Anti-Anti-Spider/tree/master/6.爬虫项目源码/17.淘宝关键词采集器

博客原文：urlteam    https://www.urlteam.org/2017/04/淘宝商品信息采集器二，开放源码可自定义关键词/
