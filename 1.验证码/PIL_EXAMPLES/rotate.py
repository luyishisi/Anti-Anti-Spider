# coding:utf-8
from __future__ import print_function
#from PIL import Image
import Image
#import glob, os



#size = 128,128
# 打开图片
#im = Image.open("11.png")
# 旋转45度 并且 显示

# im.rotate(45).show()

# 遍历该目录下的所有PNG文件，打开并且创建略缩图
# for infile in glob.glob("*.png"):
#     file,ext = os.path.splitext(infile)
# #    print file,ext
#     im = Image.open(infile)
#     im.thumbnail(size,Image.ANTIALIAS)
#     #im.save(file+".thumbnail","JPEG")

# 创建新图片，并保存
# 101 31
#new_img = Image.new("RGB",(101,31),"white")
#new_img.save("NEW.png")
# im_2 = Image.open("1.1.png")
#im_3 = Image.composite(im.copy(),im_2.copy(),'L')

# 将im与im_2 根据透明度进行合并
#im_compound = Image.blend(im.copy(),im_2.copy(),1)
#im_compound.save("3.png")

#将im_2转换为灰度图
#im_2.convert('L').save('1_convert.png')
#输出im的边框rgb
#print im_2.getbbox()
#输出im的最大最小rgb
#print im_2.getextrema()

im = Image.open('11.png')
#im = im.convert('L')
#im = im.resize((32,32),Image.ANTIALIAS)
#im.save('11_l.png')
for i in xrange(im.size[0]):
    for j in xrange(im.size[1]):

        print im.getpixel((i,j))
        l = im.getpixel((j,i))
        if( l > 220):
            print ('0',end='')
        else :
            print ('1',end='')
        if(j == im.size[0]-1):
            print ('\n',end='')
