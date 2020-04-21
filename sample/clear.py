# -*- encoding:utf-8 -*-
'''
转换图片形状，以适应CNN网络的输入
'''
import shutil
import os
from PIL import Image



def convertjpg(jpgfile, outdir, width=227,height=227):
    '''转换图片分辨率'''
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        if img.mode == "P" or img.mode == "RGBA":
            new_img = new_img.convert('RGB')
        new_img.save(outdir)
    except Exception as e:
        print("图片转换失败",e)

train_list = os.listdir('train')
for per in train_list:
    jpgfile = "train/{}".format(per)
    convertjpg(jpgfile,jpgfile)
#
# test_list = os.listdir('test')
# for per in test_list:
#     jpgfile = "test/{}".format(per)
#     convertjpg(jpgfile, jpgfile)
