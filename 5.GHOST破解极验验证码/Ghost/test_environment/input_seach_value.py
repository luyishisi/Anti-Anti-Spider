#!/usr/bin/env python
#coding:utf-8

from ghost import Ghost, Session
import time
if __name__ == '__main__':
    gh = Ghost()
    se = Session(gh, display = True)
    se.open("https://www.baidu.com/")
    se.show()#完成输入后要刷新
    se.fill("#kw","hello world")
    se.click("#su",btn=0) 
    se.show()#完成输入后要刷新
    time.sleep(10)

