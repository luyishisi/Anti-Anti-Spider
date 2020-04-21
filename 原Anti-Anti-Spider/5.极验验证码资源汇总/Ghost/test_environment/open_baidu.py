#!/usr/bin/env python
#coding:utf-8

from ghost import Ghost, Session
import time
gh = Ghost()
se = Session(gh, display = True)
se.open("https://www.baidu.com/")
time.sleep(10)

