#coding:utf-8
import time
import signal

def test(i):
    time.sleep(0.999)
    print "%d within time"%(i)
    return i

def fuc_time(time_out):
    # 此为函数超时控制，替换下面的test函数为可能出现未知错误死锁的函数
    def handler(signum, frame):
        raise AssertionError
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(time_out)#time_out为超时时间
        temp = test(1) #函数设置部分，如果未超时则正常返回数据，
        return temp
    except AssertionError:
        print "%d timeout"%(i)# 超时则报错

if __name__ == '__main__':
    for i in range(1,10):
        fuc_time(1)
