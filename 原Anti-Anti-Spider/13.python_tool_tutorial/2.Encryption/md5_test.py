import hashlib
m = hashlib.md5()
m.update(b'123')
test1 = m.hexdigest()
print(test1)
#'202cb962ac59075b964b07152d234b70'
# 或者可以这样
test2 = hashlib.md5(b'123').hexdigest()
print(test2)
#'202cb962ac59075b964b07152d234b70'
# 也可以使用hash.new()这个一般方法
test3 = hashlib.new('md5', b'123').hexdigest()
print(test3)
#'202cb962ac59075b964b07152d234b70'



#以上是对于英文进行md5加密的，如果要对中文进行加密，发现按照上面来写会报错，原因在于字符转码问题，要如下

data = '你好'
test4 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
#'7eca689f0d3389d9dea66ae112e5cfd7'
print(test4)
