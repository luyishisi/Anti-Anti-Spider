import subprocess
from threading import Timer
import time

kill = lambda process: process.kill()

cmd = ["ping", "www.google.com"]
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_timer = Timer(5, kill, [ping])
try:
    my_timer.start()
    stdout, stderr = ping.communicate()
    #print stderr
    print time.ctime()
finally:
    print time.ctime()
    my_timer.cancel()
