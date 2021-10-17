"""
验证图片尺寸和分离测试集（5%）和训练集（95%）
初始化的时候使用，有新的图片后，可以把图片放在new目录里面使用。
"""

import os
import time
import datetime
import json
import random
import os.path
import shutil

import pymysql
from PIL import Image


def convertjpg(jpgfile, outdir, width=227, height=227):
    '''转换图片分辨率'''
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        if img.mode == "P" or img.mode == "RGBA":
            new_img = new_img.convert('RGB')
        new_img.save(outdir)
    except Exception as e:
        print("图片转换失败",e)

def spilt_train_test(origin_dir,train_dir,test_dir):
    '''将样本集分成9：1'''
    img_list = os.listdir(origin_dir)
    random.seed(time.time())
    random.shuffle(img_list)
    R = int(len(img_list)*0.1)
    for file_name in img_list[:R]:
        src = os.path.join(origin_dir, file_name)
        dst = os.path.join(test_dir, file_name)
        shutil.move(src, dst)
    for file_name in img_list[R+1:]:
        src = os.path.join(origin_dir, file_name)
        dst = os.path.join(train_dir, file_name)
        shutil.move(src, dst)


def get_date_list(start=None, end=None):
    '''获取两日期间日期列表'''
    data_list = []
    datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
    dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
    while datestart<dateend:
        datestart+=datetime.timedelta(days=1)
        data_list.append(datestart.strftime('%Y-%m-%d'))
    return data_list


def get_label(date,typeid):
    '''从获取数据库获取标签'''
    conn = pymysql.connect(host='ip',
                                 port=3306,
                                 user='**',
                                 password='**',
                                 db='**',
                                 charset='utf8')
    cursor = conn.cursor()
    # sql = "SELECT result,savedir FROM new_ocr_dir WHERE typeid = '{0}' AND time LIKE '{1}%'".format(typeid,date)
    sql = "SELECT result,savedir FROM new_ocr_dir WHERE typeid = {0} AND time LIKE '{1}%'".format(typeid, date)
    result = ()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print("查询数据库失败：{0}".format(e))
    return result


def set_label(label, dir, typid, id, date):
    '''
    设置标签并修改图片分辨率
    :param label: 标签
    :param dir: 图片原地址
    :param outdir: 图片新地址
    '''
    outdir = "data/{1}_{2}_{3}_{4}.jpg".format(typid, date, id, label)
    convertjpg(dir, outdir, 227, 227)
    # try:
    #     with open(dir, 'rb') as f:
    #         img = f.read()
    #     with open("data/{0}/{1}_{2}_{3}_{4}.jpg".format(typid, typid, date, id, label), 'wb') as f:
    #         f.write(img)
    # except Exception:
    #     print(label, dir, typid)


def solve_lable_dir(label_dir):
    '''提取标签和地址'''
    labels = []
    dirs = []
    for per in label_dir:
        label = json.loads(per[0]).get('result','')
        dir = per[1][13:]
        labels.append(label)
        dirs.append(dir)
    return labels, dirs


def make_sample():
    '''选定日期和类别，制作带标签的样本集'''
    dates = get_date_list('2019-10-12', '2019-12-08')
    typeids = ['3200','3060','3050','3040','3000','2050','2040','2000','1050','1040']
    for typeid in typeids:
        for date in dates:
            print(date)
            label_dir = get_label(date, typeid)
            labels, dirs = solve_lable_dir(label_dir)
            for i, label in enumerate(labels):
                label = label.replace('|','#')
                dir = dirs[i]
                set_label(label, dir, typeid, i, date)


if __name__ == '__main__':
    make_sample()
    # spilt_train_test('data','train','test')
