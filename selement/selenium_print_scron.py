#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------
#   程序：selenium_screenshot.py
#   版本：0.1
#   作者：ly
#   日期：编写日期2016/11/23
#   环境: linux ubuntu 16.04
#   语言：Python 2.7.x
#   操作：python selenuium.py
#   功能：将列表中的url打开并获取屏幕截图存储到so_img中,图片已经删除,网址为内网.
#-------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys


#加载内核
driver = webdriver.Chrome()
driver.maximize_window()

#发起请求
url = ['http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.3.162.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.3.179.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.5.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.14.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.16.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.21.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.26.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.36.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.42.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.79.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.91.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.106.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.159.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.166.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.196.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.199.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.203.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.204.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=42.98.254.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.8.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.14.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.30.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.53.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.76.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.112.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.142.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.172.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.199.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.204.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.209.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.229.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.152.233.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.14.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.16.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.85.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.95.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.111.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.113.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.116.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.143.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.154.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.161.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.167.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.177.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.186.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.201.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.220.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.236.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.153.252.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.64.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.93.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.162.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.251.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.252.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.176.254.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=58.177.145.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.26.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.28.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.104.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.125.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.127.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.200.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.201.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.148.203.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.149.17.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.149.135.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=59.149.201.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.114.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.126.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.133.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.135.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.156.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.165.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.236.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.237.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.10.238.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.43.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.47.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.48.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.50.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.71.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.90.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.15.121.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.18.78.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.18.114.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.18.154.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.18.155.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.18.180.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.29.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.40.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.69.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.98.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.103.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.117.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.118.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.126.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.134.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.184.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.198.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.205.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.92.237.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.93.66.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.93.152.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.93.189.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.238.18.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.238.36.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.238.89.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.238.152.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.238.172.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.239.181.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.239.191.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.244.54.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.244.178.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=61.244.193.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.1.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.13.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.76.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.78.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.79.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.81.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.82.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.88.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.102.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.111.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.126.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.128.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.144.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.147.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.153.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.164.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.168.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.175.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.176.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.220.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.231.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.238.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.118.246.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.25.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.75.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.93.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.148.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.215.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.221.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.119.234.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.78.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.82.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.137.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.170.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.191.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.218.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.222.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.227.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.240.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=112.120.250.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.252.32.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.252.37.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.252.50.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.252.123.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.252.215.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.253.24.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.253.115.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.253.178.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.66.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.74.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.75.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.108.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.120.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.254.132.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.11.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.14.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.21.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.86.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.126.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=113.255.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.3.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.43.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.53.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.55.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.71.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.78.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.88.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.91.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.134.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.146.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.48.239.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.6.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.30.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.66.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.70.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.96.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.118.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.136.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.152.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.162.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.168.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.175.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.191.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.200.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.207.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.209.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=116.49.250.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=118.141.56.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.2.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.21.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.23.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.128.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.129.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.133.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.134.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.144.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.171.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.189.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.193.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.199.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.210.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.214.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.236.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.240.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.241.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.247.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.248.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.236.250.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.3.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.12.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.13.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.80.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.81.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.112.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.123.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.125.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.126.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.157.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.177.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.187.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.198.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.203.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.210.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.226.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.237.251.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.34.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.37.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.69.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.111.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.113.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.114.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.128.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.132.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.207.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.246.229.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.247.19.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.247.158.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.247.192.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.247.220.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=119.247.221.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.24.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.44.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.117.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.141.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.143.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.202.248.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.32.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.41.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.93.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.133.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.152.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=123.203.199.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=124.244.123.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=124.244.163.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=125.59.2.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=125.59.7.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=125.59.15.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=168.70.12.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=168.70.87.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=168.70.96.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=168.70.103.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=183.178.40.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=183.178.53.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=183.178.174.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=183.178.175.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=183.179.193.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.168.189.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.198.16.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.198.24.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.198.28.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.198.88.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.24.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.31.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.35.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.42.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.73.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.93.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.103.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.132.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.141.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.142.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.143.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.150.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.158.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.167.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.205.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.214.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.238.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.249.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=203.218.253.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.64.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.90.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.105.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.122.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.136.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.149.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.178.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.179.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.190.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.195.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.198.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.207.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.217.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.102.236.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.132.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.133.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.134.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.138.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.145.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.148.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.152.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.156.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.158.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.193.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.197.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.227.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.243.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.246.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.103.253.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.191.130.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.191.195.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.191.220.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.70.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.74.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.80.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.86.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.87.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.88.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.121.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.150.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.154.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.157.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.163.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.165.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.173.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.178.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.199.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.220.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.250.245.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=218.254.62.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.73.50.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.73.84.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.73.97.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.73.101.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.76.89.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.76.148.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.76.162.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.76.168.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.76.244.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.9.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.35.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.38.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.41.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.42.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.51.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.65.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.77.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.85.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.97.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.115.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.117.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.142.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.150.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.182.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.201.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.210.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.232.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.241.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.77.245.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.30.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.33.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.36.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.40.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.48.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.49.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.102.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.119.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.161.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.162.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.193.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.195.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.198.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.223.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.78.250.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.10.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.14.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.40.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.61.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.85.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.86.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.173.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.176.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.192.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.211.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=219.79.212.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=220.246.209.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=220.246.217.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.7.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.24.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.54.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.55.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.73.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.127.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=221.127.164.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.166.71.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.166.102.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.166.145.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.166.148.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.166.180.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.167.84.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.167.130.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=222.167.194.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.16.166.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.16.202.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.16.225.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.16.226.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.17.49.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.17.52.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.17.141.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.17.143.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.17.145.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.123.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.178.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.180.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.185.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.205.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.238.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.18.239.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.19.208.','http://192.168.1.136:8080/hk_proceess/221/ttt.jsp?ip3=223.19.218.'
]

for i in url:
    print i
    driver.get(i)
    time.sleep(3)
    ip_name = i[54::].replace('.','-')
    name = './so_img/'+ip_name+'.png'
    driver.save_screenshot(name)
    #time.sleep(1)

driver.quit()
#elem.clear()
#time.sleep(10)
#driver.close()
