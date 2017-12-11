import math
import random
import matplotlib.pyplot as plt

def getTrack(intX):
    t1 = intX*(10+random.randint(2,7))
    t0 = 0
    g = lambda t:math.tanh(1.5*(t-t0)/(t1-t0))
    track_raw = []
    for t in range(t1):
        track_raw.append(int(intX/g(t1)*g(t)))

    index = 0
    track = []
    while index < len(track_raw):
        show = track_raw[index + min(10,len(track_raw) - index - 1)] - track_raw[index]
        #print(len(track_raw)-index)
        index += 10
        track.append(show)

    return track

if __name__ == "__main__":
    t = getTrack(int(82.49752629528632))
    print(t)
    y = []
    x = []
    now = 0
    a = 0
    for i in t:
        a+=random.randint(1,2)
        x.append(a)
        y.append(now)
        now += i
    plt.plot(x,y)
    plt.show()