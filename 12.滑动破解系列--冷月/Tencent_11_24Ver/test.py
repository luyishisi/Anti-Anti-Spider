from Crypto.Cipher import AES
import base64
import json
import collections
import time
import random

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

#raw = str(input())
raw = "HkMJa9JO8Vo/mYA/c4IqRaERxVSvgqxq8jkZCMrAqBzGfCzR8DpScz17BgcDhgaEH5jw/J/YYj/ZF85BBJHEb52dW0iYHpxfJAcd9cn8KZ6t8a09FB8ARBtwUT9TF3M9KCsIjDF286aM0exIwbIbqUY0s2EH0mjv1pZ75cu51394Aynj6rrz5XOG4qe7UHLlsUqBVV7wvicc5nGIpqF5t86SVp6gk5H9X6p1gvcEGJWnzEPipqPZgdslcQ5eeFbOu9HAHejgo2oGMHlN62Or6U1SlAvizl/pOp8Wf2b9Hxh9wPwT94FCYqRWtom/w9jEwc/03Zpee1e4f104GkdvUqWsTBI11CpnuzHAVYmSKWvI/fAX/SAzEWTKTCoDftsbbl7Mwdv6M18sYeqR3mCmPDtnPBdKa7gy+j4Qe2p2wJ5dZ2PgCEjhHL8Ic0cxP572VzIMFOk5Luv7utVLyBY30tUgLXANpFlnEW+AHmg3wCl8RJXY7z/ZUw49u520Hk1kxfi7Bz4dlHBa3bNYZDw2vblOmkFRUcZi1wrdMRHgt4PnFTXPmej8lqV6G+OOXbgGm4QkSjtpXH7o6zMprHI8WR7+FdL4QIZ5Bm64gcf/G9uL6bsA/6VC7/g5dcDGjjuM9q30X1KWMQU23K/0BECcCwZFWQOMWbhZ8CjbYyEvXNTNr7mwftCDcF7tKtDA+KPN3U8KYd1OyO7o/bVcY6MdzZuyQ/NX9OTWrdOfmqiyrMIitwpxveUN0MnDz20Qf5hTQlW7bAoT/EoOKaazbWesf9HPJ3eWSh4zEUO/h1PI9Wrevhk/fjLI7Z3ZKAy2+NyboSKrkLVK71dBClfQ+aAIT3LBehPPzRInjEaZ8oFqxWu9JuKsJ4+bcrEHQn9SlUxrD6J1DyXVszyQgh/XgzqtTPKSjTHtE1g1soB7CA/sOl1k0Yiah/14i6k+wkfuDrqRMWbwDiPjwqfCV99IYMReAJPRwZRyF4mEvu/PPsyp4rMRoCr2dH9GA6DnJWT0ksRLdS2byKcX+W0Q6MCsZ1/5OTUIXQ+szjWalvo9A9+hsaTF2mxYeGtFVSZ9REhARJ5N9K1lW6EMHASbCQMyNDaHWxonbR11z2PuDFDz9Z6eS3/E+weZlXbl5XHkTQh+F6V/Q/fPw9xm+2JOk0HbyhvSK9UIP0PjHOHj8zXKBV1qu0EZbHdKMpNc5dkiBWeylxOZYZ5+6qcVRlnhqJBuzQtQydeVhiuVqOaIiGCRbNys1v3+io8eoew5AcY2hcFICf/9HyjqQmEFbbfcq6uyJGceyfywm0ROYKlNz0S5Kmn0EKJRqw8y9rlK+qaevu9LJar+qlvYCxaW0BUe9GdsF3ePx+4XD2a9Z/1LCPfcTkDJNEJVboVgYPpwtBaZkFoi2SnSiiMrJrH8HXdMslPiTD4Lp1vNFGAWX4b2XVPxAfWrhaYQDplQTYhJrbel6Vx5jraAXrOAZNZCSrwu15C2rRiAo8QD6bMo2qugNFCQjU3BVfxU1EKH67nMzlWbHhvI37bXH61skdXFdMWD9v3srPKWQYmuwsKSGNyUxi7jSGv+O021XWbahmgU0/Oz+faEKkNBLlrgxUIQ6No="
raw = base64.b64decode(raw)
while len(raw)%16!=0:
    raw = raw + " ".encode()
cipher = AES.new("i735CQhyGf8y7Z34", AES.MODE_CBC, "i735CQhyGf8y7Z34")
decrypted = cipher.decrypt(raw)
print(decrypted.decode("utf-8","ignore"))
exit()
res = decrypted.decode()
j = json.loads(unpad(res), object_pairs_hook= collections.OrderedDict)
"""
j["begintime"] = int(time.time()) - 2
j["endtime"] = int(time.time())
token_random = "187246" + str(random.randint(1000,9999))
j["tokenid"] = token_random
j["a"] = token_random
j["tokents"] = int(time.time()) - 2
"""
#j["ips"]["in"] = ['172.16.2.' + str(random.randint(0,254))]#OrderedDict([('in', ['172.16.2.106'])]))
print(j)
json_dump = json.dumps(j)
wbd = json_dump.replace(" ","")
for i in range(15 - len(wbd) % 16):
    wbd = wbd + " "

cipher = AES.new("0123456789abcdef", AES.MODE_CBC, "0123456789abcdef")
encoded = base64.b64encode(cipher.encrypt(pad(wbd))).decode()
print(encoded)
