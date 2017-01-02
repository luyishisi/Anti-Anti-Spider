#coding:utf-8
import Image
from PIL import Image


def image_joint(image_list,opt):#opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num=len(image_list)
    image_size=image_list[0].size
    height=image_size[1]
    width=image_size[0]
    if opt=='vertical':
        new_img=Image.new('RGB',(width,image_num*height),255)
    else:
        new_img=Image.new('RGB',(image_num*width,height),255)
    x=y=0
    count=0
    for img in image_list:
        new_img.paste(img,(x,y))
        count+=1
        if opt=='horizontal':
            x+=width
        else : y+=height

    new_img.show()
    new_img.save('1.png')
    return new_img

if __name__ == '__main__':
    opt = 'vertical'
    img=Image.open('Sun-Jan--1-14:52:21-2017.png')
    img1=Image.open('Sun-Jan--1-14:52:21-2017.png')
    image_list = [img,img1]
    print "begin"
    image_joint(image_list,opt)
