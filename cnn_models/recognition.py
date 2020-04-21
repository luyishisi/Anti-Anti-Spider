# -*- encoding: utf-8 -*-

import os
import numpy as np
import json

import tensorflow as tf
from PIL import Image

from cnn_models.cnn_model import CNN

os.environ["CUDA_VISIBLE_DEVICES"] = "1"


class Recognizer(CNN):
    def __init__(self, image_height, image_width, max_captcha, char_set, model_save_dir):
        super(Recognizer, self).__init__(image_height, image_width, max_captcha, char_set, model_save_dir)
        self.g = tf.Graph()
        self.sess = tf.Session(graph=self.g)
        with self.g.as_default():
            # 始化占位符
            self.X = tf.placeholder(tf.float32, [None, self.image_height * self.image_width])  # 图片向量
            self.Y = tf.placeholder(tf.float32, [None, self.max_captcha * self.char_set_len])  # 标签
            self.keep_prob = tf.placeholder(tf.float32)  # dropout值
            # 加载网络和模型参数
            self.y_predict = self.alexnet_model()
            # self.y_predict = self.Letnet_model()
            self.predict = tf.argmax(tf.reshape(self.y_predict, [-1, self.max_captcha, self.char_set_len]), 2)
            saver = tf.train.Saver()
            with self.sess.as_default() as sess:
                saver.restore(sess, self.model_save_dir)


    def rec_image(self, img):
        '''
        利用训练好的模型识别图片
        :param img: 验证码图片
        :return: 验证码结果
        '''
        # 读取图片
        img_array = np.array(img)
        image = self.convert2gray(img_array)
        image = image.flatten() / 255

        with self.g.as_default():
            with self.sess.as_default() as sess:
                text_list = sess.run(self.predict, feed_dict={self.X: [image], self.keep_prob: 1.})

        # 得到结果
        predict_text = text_list[0].tolist()
        text = ""
        for p in predict_text:
            text += str(self.char_set[p])
        return text


def main():
    with open("../conf/config.json", "r", encoding="utf-8") as f:
        sample_conf = json.load(f)
    image_height = sample_conf["image_height"]
    image_width = sample_conf["image_width"]
    max_captcha = sample_conf["max_captcha"]
    char_set = sample_conf["char_set"]
    model_save_dir = '../model_result/'
    R = Recognizer(image_height, image_width, max_captcha, char_set, model_save_dir)
    train_list = os.listdir('../sample/train')
    cnt = 0
    for per in train_list:
        jpgfile = "../sample/train/{}".format(per)
        label = per.split('_')[-1].replace('.jpg','')
        r_img = Image.open(jpgfile)  #
        t = R.rec_image(r_img)
        if label == t:
            cnt += 1
        # print(label,t)
    print(cnt/len(train_list))

    # r_img = Image.open("E:\\新建文件夹\\train\\3040_2019-12-02_253_0969.jpg")
    # r_img = r_img.resize((227, 227), Image.BILINEAR)
    #
    # t = R.rec_image(r_img)
    # print(t)


if __name__ == '__main__':
    main()

