#coding:utf-8
import Image

def Noise(img,i,j):
    #导入图像和ij，测试该点是否是噪点
    num = 0

    for temp_i in [-1,0,1]:
        for temp_j in [-1,0,1]:
            try:
                if img.getpixel((i+temp_j,j+temp_j)) != img.getpixel((i,j)):
                    num += 1
                #    print img.getpixel((i,j))
            except:
                #print '11'
                pass
    if num == 6:
        return 1 #如果周围8个点均与该点不同则该点为噪点
    else :
        return 0

def cat_img(im,name):

    box = (0,0,101,31)
    im = im.crop(box)#切割
    #im.show()
    box = (0,0,26,30)
    im1 = im.crop(box)#.convert('L')#切割
    #im1.show() #第一个数字
    box = (26,0,41,30)
    im2 = im.crop(box)#.convert('L')#切割
    #im2.show()# 运算符号
    box = (41,0,65,30)
    im3 = im.crop(box)#.convert('L')#切割
    #im3.show()# 第二个数字
    #region.show()
    #(101, 31) {'0-0-255': 16, '0-255-0': 58, '255-0-0': 95, '68-146-137': 2899, '255-255-255': 63}                                      
    print im.size
#    rgb_dic = {}

    # 二值化第一个数字
    min_j_1 = 30
    max_j_1 = 0
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            r,g,b = im1.getpixel((i,j))
            if r == 255 and b != 255:
                if min_j_1 > j:
                    min_j_1 = j
                max_j_1 = j
                im1.putpixel((i,j), (0,0,0))
            else:
                im1.putpixel((i,j),(255,255,255))
    cat_num_box_1 = (0,min_j_1,26,min_j_1+10)# 未知错误用固定字高10替代
    im1 = im1.crop(cat_num_box_1)
    print min_j_1,max_j_1,cat_num_box_1
    #im1.show()
    im1_1 = im1.crop((5,0,13,10))
    im1_1.save("./temp/"+name+'_1_1.png')
    im1_2 = im1.crop((14,0,22,10))
    im1_2.save("./temp/"+name+'_1_2.png')

    # 二值化运算符号
    min_j_2 = 30
    max_j_2 = 0
    #im2.show()
    try:
        for i in range(im2.size[0]):
            for j in range(im2.size[1]-4):
                r,g,b = im2.getpixel((i,j))
                if(Noise(im2,i,j)):
                    continue

                if r == 255 and b == 255:
                    if min_j_2 > j:
                        min_j_2 = j
                    max_j_2 = j
                    im2.putpixel((i,j), (0,0,0))
                else:
                    im2.putpixel((i,j),(255,255,255))
        #im2.show()
        print min_j_2,max_j_2
        cat_num_box_2 = (0,min_j_2,14,min_j_2+10)#固定高度
        im2 = im2.crop(cat_num_box_2)
        #im2.show()
        im2.save("./temp/"+name+'_fuhao.png')
    except Exception,e:
        print e

    # # 二值化第二个数字
    min_j_3 = 30
    max_j_3 = 0
    #im3.show()
    for i in range(im3.size[0]):
        for j in range(im3.size[1]):
            r,g,b = im3.getpixel((i,j))
            if g == 255 and b != 255:
                if min_j_3 > j:
                    min_j_3 = j
                max_j_3 = j
                im3.putpixel((i,j), (0,0,0))
            else:
                im3.putpixel((i,j),(255,255,255))
    cat_num_box_3 = (0,min_j_3,24,min_j_3+10)#固定高度
    im3 = im3.crop(cat_num_box_3)
    #im3.show()
    #im3.show()
    print min_j_3,max_j_3,cat_num_box_3
    im3.save("./temp/"+name+'_2.png')
    # im3_1 = im3.crop((5,0,13,10))
    # im3_1.save("./temp/"+name+'_3_1.png')
    # im3_2 = im3.crop((14,0,22,10))
    # im3_2.save("./temp/"+name+'_3_2.png')


if __name__ == '__main__':
    for i in ['11','12','13','14','15']:
        #name = '11'
        name = i
        im = Image.open("./trins/"+name+'.png').convert('RGB')#重点要切换图片模式
        cat_img(im,name)
