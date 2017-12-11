import base64



x = '{"cd":[5,"?rand=0.6046136020818618",864,[],0,[{"t":5589,"x":148,"y":234}],1,1,"chrome/62.0.3202.94",1512478946,[],0,1510960881645,"1536-864-824-24-*-*-*","UTF-8",[[176,25,5586839],[0,7,6],[-3,10,15],[-3,42,19],[3,37,16],[15,47,16],[9,30,16],[5,14,16],[2,4,17],[0,5,16],[-4,7,20],[-8,4,14],[-11,4,16],[-5,2,17],[-8,0,20],[-2,0,13],[-4,0,20],[-1,0,13],[-1,0,17],[-2,0,48],[-1,0,9],[-1,0,10],[-3,4,18],[-1,0,17],[0,2,15],[-2,-2,433],[-2,0,83],[-4,4,17],[-6,2,17],[-2,0,17],[-2,0,16],[-2,0,17],[-4,0,20],[-2,-3,16],[-1,0,16],[-3,0,18],[-6,0,15],[-6,0,15],[-6,0,17],[-4,0,16],[-3,-1,19],[-1,0,16],[0,-2,16],[-4,-4,16],[-2,0,20],[-2,0,18],[-3,0,15],[-1,0,14],[-2,0,15],[-2,0,19],[0,0,15],[-3,0,17],[-1,-1,16],[0,-1,17],[0,0,18],[-3,0,76],[-1,-2,88],[0,0,84],[0,-1,61],[1,0,8],[7,0,15],[16,-1,18],[16,-2,16],[14,0,16],[8,0,17],[4,0,16],[3,0,17],[3,2,20],[2,2,17],[2,0,13]],[258,759],"other",12,[{"x":0,"y":0,"z":0},{"x":0,"y":0,"z":0},{"x":0,"y":0,"z":0},{"x":0,"y":0,"z":0}],1512473355,1536,24,1,0,[],1,0,null,true,["zh-CN","zh"],14,{"in":["172.20.10.2"]},[{"t":5587,"x":164,"y":236}],"https://ssl.captcha.qq.com/cap_union_new_show",27,8,754176585,1511510573,"906622a97db3f72f7d0815d20c8c93b68d79f23755321896cfd47f67e6f7c4df"],"sd":{"od":"AgAAAB","ft":"6f_7P_n_H","clientType":"1","coordinate":[116,124,0.4294],"trycnt":4,"refreshcnt":0,"slideValue":[[72,234,4],[0,-1,60],[1,0,8],[7,0,15],[16,-1,18],[16,-2,17],[14,0,15],[8,0,17],[4,0,16],[3,0,17],[3,2,21],[2,2,16],[2,0,13],[0,0,50]],"jshook":4}};'

e = "e2ckQHrXitpbBxb5"

"""
function c(x) {
    for (var e = 0, n = 0; t[_0x50e8("0x37b", "nD55")](n, 4); n++)
        e |= t[_0x50e8("0x37c", "FX^#")](x[_0x50e8("0x37d", "JwF&")](n), 8 * n);
    return isNaN(e) ? 0 : e
}
"""
def c(x):
    temp = 0
    try:
        for n in range(4):
            temp |= ord(x[n]) << 8 * n
    except:
        return 0
    return temp

"""
function w(x, e) {
    for (var n = x[0], w = x[1], c = t[_0x50e8("0x373", "cx[G")](2654435769, 32), r = 0; r != c; )
        n += t[_0x50e8("0x374", "lDL4")]((w << 4 ^ t[_0x50e8("0x375", "m5cV")](w, 5)) + w, r + e[3 & r]),
        r += 2654435769,
        w += t[_0x50e8("0x376", "yXWm")](t[_0x50e8("0x377", "0qS[")](t[_0x50e8("0x378", "nD55")](n << 4, n >>> 5), n), t[_0x50e8("0x379", "qk7Q")](r, e[3 & t[_0x50e8("0x37a", "DzfY")](r, 11)]));
    x[0] = n,
    x[1] = w
}
"""

def unsigned_right_shift(n,i):

    return int(n & (2**32-1)) >> i

def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val

#妈耶心态崩了啊

def w(x,e):
    a = x[0]
    b = x[1]
    c = 2654435769 * 32
    r = 0
    while r != c:
        #print(a, r, b)
        a += int_overflow(int_overflow(((int_overflow(b << 4) ^ unsigned_right_shift(b,5)) + b ^ r + e[3 & r])))
        #print(((int_overflow(b << 4) ^ unsigned_right_shift(b,5)) + b),(r + e[3 & r]))
        r += 2654435769
        b += int_overflow((int_overflow(a << 4) ^ unsigned_right_shift(a,5)) + a ^ r + e[3 & unsigned_right_shift(r,11)])

    x[0] = a
    x[1] = b


"""
zz = [1684218491, 895171106]
e = [1801663077, 1483884625, 1651537001, 895645762]
w(zz,e)
print(zz)
exit()


function r(x) {
        return String[_0x50e8("0x37e", "lNS$")](255 & x, 255 & t[_0x50e8("0x37f", "lNS$")](x, 8), x >> 16 & 255, x >> 24 & 255)
    }
"""

def r(x):
    return str(chr(255 & x)) + str(chr(255 & unsigned_right_shift(x,8))) + str(chr(unsigned_right_shift(x,16) & 255))\
           + str(chr(unsigned_right_shift(x,24) & 255))

"""
print(r(5757834321))
print(base64.b64encode(r(5757834321).encode()))
exit()

for (var n = new Array(2), o = new Array(4), u = "", i = 0; i < 4; i++)
    o[i] = t[_0x50e8("0x368", "(Vv4")](c, e[_0x50e8("0x369", "JwF&")](4 * i, 4 * (i + 1)));
    
"""

u = ""
n = [0,0]
o = []
for i in range(4):
    sb = e[i:i+4]
    o.append(c(sb))


"""
for (i = 0; t[_0x50e8("0x36a", "qk7Q")](i, x[_0x50e8("0x36b", "qk7Q")]); i += 8)
    n[0] = t[_0x50e8("0x36c", "jT%F")](c, x[_0x50e8("0xeb", "jT%F")](i, i + 4)),
    n[1] = t[_0x50e8("0x36d", "deNc")](c, x[_0x50e8("0x36e", "940m")](t[_0x50e8("0x36f", "ljOP")](i, 4), t[_0x50e8("0x370", "6IIS")](i, 8))),
    t[_0x50e8("0x371", "!M&C")](w, n, o),
    u += r(n[0]) + r(n[1]);
"""

i = 0
while i < len(x):
    n[0] = c(x[i:i+4])
    n[1] = c(x[i+4:i+8])
    #print(x[i:i + 4], x[i + 4:i + 8])
    if n[0] > 2147483647 or n[1]>2147483647:
        print(n)
    w(n,o)
    u += r(n[0]) + r(n[1])
    #print(str(r(n[0])) + str(r(n[1])))
    #print(u)

    i += 8

print(base64.b64encode(u.encode()))