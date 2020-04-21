# encoding:utf-8

import numpy as np
import random

import tensorflow as tf
from PIL import Image

class CNN(object):

    def __init__(self, image_height, image_width, max_captcha, char_set, model_save_dir):
        self.image_height = image_height  # 图片高度
        self.image_width = image_width  # 图片宽度
        self.char_set = char_set  # 字符集
        self.char_set_len = len(char_set)  # 字符集大小
        self.max_captcha = max_captcha  # 验证码字符长度
        self.model_save_dir = model_save_dir  # 模型路径
        with tf.name_scope('parameters'):
            self.w_alpha = 0.01
            self.b_alpha = 0.1
        with tf.name_scope('data'):
            self.X = tf.placeholder(tf.float32, [None, self.image_height * self.image_width])  # 特征向量
            self.Y = tf.placeholder(tf.float32, [None, self.max_captcha * self.char_set_len])  # 标签
            self.keep_prob = tf.placeholder(tf.float32)  # dropout值

    @staticmethod
    def convert2gray(img):
        """
        图片转为灰度图
        """
        if len(img.shape) > 2:
            r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            return gray
        else:
            return img

    def text2vec(self, text):
        """
        转标签为oneHot编码
        """
        text_len = len(text)
        if text_len > self.max_captcha:
            raise ValueError('验证码最长{}个字符'.format(self.max_captcha))

        vector = np.zeros(self.max_captcha * self.char_set_len)

        for i, ch in enumerate(text):
            idx = i * self.char_set_len + self.char_set.index(ch)
            vector[idx] = 1
        return vector

    def alexnet_model(self):
        '''CNN模型，输入为self.X,输入为y_predict'''
        x = tf.reshape(self.X, shape=[-1, self.image_height, self.image_width, 1])

        with tf.name_scope("conv1") as scope:
            kernel1 = tf.Variable(tf.truncated_normal([11, 11, 1, 96], mean=0, stddev=0.1,
                                                      dtype=tf.float32))
            conv = tf.nn.conv2d(x, kernel1, [1, 4, 4, 1], padding="SAME")
            biases = tf.Variable(tf.constant(0, shape=[96], dtype=tf.float32), trainable=True)
            bias = tf.nn.bias_add(conv, biases)
            conv1 = tf.nn.relu(bias)
            lrn1 = tf.nn.lrn(conv1, 4, bias=1, alpha=1e-3 / 9, beta=0.75)
            pool1 = tf.nn.max_pool(lrn1, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding="VALID")

        with tf.name_scope('conv2') as scope:
            kernel2 = tf.Variable(tf.truncated_normal([5, 5, 96, 256], mean=0, stddev=0.1,
                                                      dtype=tf.float32))
            conv = tf.nn.conv2d(pool1, kernel2, [1, 1, 1, 1], padding="SAME")
            biases = tf.Variable(tf.constant(0, shape=[256], dtype=tf.float32), trainable=True)
            bias = tf.nn.bias_add(conv, biases)
            conv2 = tf.nn.relu(bias)
            lrn2 = tf.nn.lrn(conv2, 4, bias=1, alpha=1e-3 / 9, beta=0.75)
            pool2 = tf.nn.max_pool(lrn2, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding="VALID")

        with tf.name_scope('conv3') as scope:
            kernel3 = tf.Variable(tf.truncated_normal([3, 3, 256, 384], mean=0, stddev=0.1,
                                                      dtype=tf.float32))
            conv = tf.nn.conv2d(pool2, kernel3, [1, 1, 1, 1], padding="SAME")
            biases = tf.Variable(tf.constant(0, shape=[384], dtype=tf.float32), trainable=True)
            bias = tf.nn.bias_add(conv, biases)
            conv3 = tf.nn.relu(bias)

        with tf.name_scope('conv4') as scope:
            kernel4 = tf.Variable(tf.truncated_normal([3, 3, 384, 384], mean=0, stddev=0.1,
                                                      dtype=tf.float32))
            conv = tf.nn.conv2d(conv3, kernel4, [1, 1, 1, 1], padding="SAME")
            biases = tf.Variable(tf.constant(0, shape=[384], dtype=tf.float32), trainable=True)
            bias = tf.nn.bias_add(conv, biases)
            conv4 = tf.nn.relu(bias)

        with tf.name_scope('conv5') as scope:
            kernel5 = tf.Variable(tf.truncated_normal([3, 3, 384, 256], mean=0, stddev=0.1,
                                                      dtype=tf.float32))
            conv = tf.nn.conv2d(conv4, kernel5, [1, 1, 1, 1], padding="SAME")
            biases = tf.Variable(tf.constant(0, shape=[256], dtype=tf.float32), trainable=True)
            bias = tf.nn.bias_add(conv, biases)
            conv5 = tf.nn.relu(bias)
            pool5 = tf.nn.max_pool(conv5, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding="VALID")

        with tf.name_scope('fc1') as scope:
            pool5 = tf.reshape(pool5, (-1, 6 * 6 * 256))
            weight6 = tf.Variable(tf.truncated_normal([6 * 6 * 256, 4096], stddev=0.1, dtype=tf.float32))
            ful_bias1 = tf.Variable(tf.constant(0.0, dtype=tf.float32, shape=[4096]), name="ful_bias1")
            ful_con1 = tf.nn.relu(tf.add(tf.matmul(pool5, weight6), ful_bias1))

        with tf.name_scope('fc2') as scope:
            weight7 = tf.Variable(tf.truncated_normal([4096, 4096], stddev=0.1, dtype=tf.float32))
            ful_bias2 = tf.Variable(tf.constant(0.0, dtype=tf.float32, shape=[4096]), name="ful_bias2")
            ful_con2 = tf.nn.relu(tf.add(tf.matmul(ful_con1, weight7), ful_bias2))

        with tf.name_scope('fc3') as scope:
            weight8 = tf.Variable(tf.truncated_normal([4096, 1000], stddev=0.1, dtype=tf.float32),
                                  name="weight8")
            ful_bias3 = tf.Variable(tf.constant(0.0, dtype=tf.float32, shape=[1000]), name="ful_bias3")
            ful_con3 = tf.nn.relu(tf.add(tf.matmul(ful_con2, weight8), ful_bias3))

        with tf.name_scope('y_prediction'):
            weight9 = tf.Variable(tf.truncated_normal([1000, self.char_set_len*self.max_captcha], stddev=0.1), dtype=tf.float32)
            bias9 = tf.Variable(tf.constant(0.0, shape=[self.char_set_len*self.max_captcha]), dtype=tf.float32)
            y_predict = tf.matmul(ful_con3, weight9) + bias9


        return y_predict

    def Letnet_model(self):
        '''CNN模型，输入为self.X,输入为y_predict'''
        x = tf.reshape(self.X, shape=[-1, self.image_height, self.image_width, 1])

        # w_c1_alpha = np.sqrt(2.0/(IMAGE_HEIGHT*IMAGE_WIDTH)) #
        # w_c2_alpha = np.sqrt(2.0/(3*3*32))
        # w_c3_alpha = np.sqrt(2.0/(3*3*64))
        # w_d1_alpha = np.sqrt(2.0/(8*32*64))
        # out_alpha = np.sqrt(2.0/1024)

        # 3 conv layer
        w_c1 = tf.Variable(self.w_alpha * tf.random_normal([3, 3, 1, 32]))  # 从正太分布输出随机值
        b_c1 = tf.Variable(self.b_alpha * tf.random_normal([32]))
        conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, w_c1, strides=[1, 1, 1, 1], padding='SAME'), b_c1))
        conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv1 = tf.nn.dropout(conv1, self.keep_prob)

        w_c2 = tf.Variable(self.w_alpha * tf.random_normal([3, 3, 32, 64]))
        b_c2 = tf.Variable(self.b_alpha * tf.random_normal([64]))
        conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1, w_c2, strides=[1, 1, 1, 1], padding='SAME'), b_c2))
        conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv2 = tf.nn.dropout(conv2, self.keep_prob)

        w_c3 = tf.Variable(self.w_alpha * tf.random_normal([3, 3, 64, 64]))
        b_c3 = tf.Variable(self.b_alpha * tf.random_normal([64]))
        conv3 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv2, w_c3, strides=[1, 1, 1, 1], padding='SAME'), b_c3))
        conv3 = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv3 = tf.nn.dropout(conv3, self.keep_prob)

        # Fully connected layer
        w_d = tf.Variable(self.w_alpha * tf.random_normal([8 * 20 * 64, 1024]))
        b_d = tf.Variable(self.b_alpha * tf.random_normal([1024]))
        dense = tf.reshape(conv3, [-1, w_d.get_shape().as_list()[0]])
        dense = tf.nn.relu(tf.add(tf.matmul(dense, w_d), b_d))
        dense = tf.nn.dropout(dense, self.keep_prob)

        w_out = tf.Variable(self.w_alpha * tf.random_normal([1024, self.char_set_len * self.max_captcha]))
        b_out = tf.Variable(self.b_alpha * tf.random_normal([self.char_set_len * self.max_captcha]))
        y_predict = tf.add(tf.matmul(dense, w_out), b_out)
        # out = tf.nn.softmax(out)
        return y_predict