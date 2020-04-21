# encoding:utf-8

import os
import time
import json
import random


from PIL import Image
import numpy as np
import tensorflow as tf

from cnn_models.cnn_model import CNN


class train_model(CNN):
    def __init__(self, train_img_path, verify_img_path, char_set, model_save_dir, cycle_stop, acc_stop, cycle_save,
                 train_batch_size, test_batch_size):

        self.cycle_stop = cycle_stop  # 循环次数
        self.acc_stop = acc_stop  # 达到准确率停止
        self.cycle_save = cycle_save  # 当前循环次数
        self.train_batch_size = train_batch_size  # 训练批大小
        self.test_batch_size = test_batch_size  # 测试批大小
        char_set = [str(i) for i in char_set]

        self.train_img_path = train_img_path
        self.train_images_list = os.listdir(train_img_path)

        # 打乱文件顺序
        random.seed(time.time())
        random.shuffle(self.train_images_list)

        # 验证集文件
        self.verify_img_path = verify_img_path
        self.verify_images_list = os.listdir(verify_img_path)

        # 获得图片宽高和字符长度基本信息
        label, captcha_array = self.gen_captcha_text_image(train_img_path, self.train_images_list[0])

        captcha_shape = captcha_array.shape
        captcha_shape_len = len(captcha_shape)
        if captcha_shape_len == 3:
            image_height, image_width, channel = captcha_shape
            self.channel = channel
        elif captcha_shape_len == 2:
            image_height, image_width = captcha_shape
        else:
            raise Exception("图片转换为矩阵时出错，请检查图片格式")

        # 初始化变量
        super(train_model, self).__init__(image_height, image_width, 4, char_set, model_save_dir)

        # 相关信息打印
        print("-->图片尺寸: {} X {}".format(image_height, image_width))
        print("-->验证码长度: {}".format(self.max_captcha))
        print("-->验证码共{}类 {}".format(self.char_set_len, char_set))
        print("-->使用测试集为 {}".format(train_img_path))
        print("-->使验证集为 {}".format(verify_img_path))

        # test model input and output
        print(">>> Start model test")
        batch_x, batch_y = self.get_train_batch(0, size=100)
        print(">>> input batch images shape: {}".format(batch_x.shape))
        print(">>> input batch labels shape: {}".format(batch_y.shape))

    @staticmethod
    def gen_captcha_text_image(img_path, img_name):
        """
        返回一个验证码的array形式和对应的字符串标签
        :return:tuple (str, numpy.array)
        """
        # 文件
        label = img_name.split("_")[-1].replace('.jpg','')
        # 文件
        img_file = os.path.join(img_path, img_name)
        captcha_image = Image.open(img_file)
        captcha_array = np.array(captcha_image)  # 向量化
        return label, captcha_array


    def get_train_batch(self, n, size=64):
        batch_x = np.zeros([size, self.image_height * self.image_width])  # 初始化
        batch_y = np.zeros([size, self.max_captcha * self.char_set_len])  # 初始化

        max_batch = int(len(self.train_images_list) / size)
        # print(max_batch)
        if max_batch - 1 < 0:
            raise Exception("训练集图片数量需要大于每批次训练的图片数量")
        if n > max_batch - 1:
            n = n % max_batch
        s = n * size
        e = (n + 1) * size
        this_batch = self.train_images_list[s:e]
        # print("{}:{}".format(s, e))

        for i, img_name in enumerate(this_batch):
            label, image_array = self.gen_captcha_text_image(self.train_img_path, img_name)
            image_array = self.convert2gray(image_array)  # 灰度化图片
            batch_x[i, :] = image_array.flatten() / 255  # flatten 转为一维
            batch_y[i, :] = self.text2vec(label)  # 生成 oneHot
        return batch_x, batch_y

    def get_verify_batch(self, size=50):
        batch_x = np.zeros([size, self.image_height * self.image_width])  # 初始化
        batch_y = np.zeros([size, self.max_captcha * self.char_set_len])  # 初始化

        verify_images = []
        for i in range(size):
            # TODO:
            verify_images.append(random.choice(self.train_images_list))

        for i, img_name in enumerate(verify_images):
            # TODO:
            label, image_array = self.gen_captcha_text_image(self.train_img_path, img_name)
            image_array = self.convert2gray(image_array)  # 灰度化图片
            batch_x[i, :] = image_array.flatten() / 255  # flatten 转为一维
            batch_y[i, :] = self.text2vec(label)  # 生成 oneHot
        return batch_x, batch_y

    def train(self):
        y_pred = self.alexnet_model()
        # y_pred = self.Letnet_model()
        print(">>>input batch predict shape:{}".format(y_pred.shape))
        print(">>>End model test")
        # 计算损失函数
        with tf.name_scope('cost'):
            cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=y_pred, labels=self.Y))
        # 梯度下降法
        with tf.name_scope('train'):
            optimizer = tf.train.GradientDescentOptimizer(0.000008).minimize(cost)
        # 计算准确率
        predict = tf.reshape(y_pred, [-1, self.max_captcha, self.char_set_len])
        max_idx_p = tf.argmax(predict, 2)  # 返回在张量轴上具有最大值的索引
        max_idx_l = tf.argmax(tf.reshape(self.Y, [-1, self.max_captcha, self.char_set_len]), 2)  #
        # 计算准确率
        correct_pred = tf.equal(max_idx_p, max_idx_l)
        with tf.name_scope('char_acc'):
            accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
        with tf.name_scope('image_acc'):
            accuracy_image_count = tf.reduce_mean(tf.reduce_min(tf.cast(correct_pred, tf.float32), axis=1))
        init = tf.global_variables_initializer()
        saver = tf.train.Saver()
        # 设置模型存储路径

        config = tf.ConfigProto()
        config.gpu_options.per_process_gpu_memory_fraction = 0.7

        with tf.Session(config=config) as sess:
            init = tf.global_variables_initializer()
            sess.run(init)
            # 导入模型
            if os.path.exists(self.model_save_dir):
                try:
                    saver.restore(sess, self.model_save_dir)
                except:
                    print('model文件夹为空')

            tf.summary.FileWriter("logs/", sess.graph)
            step = 1
            for i in range(self.cycle_stop):
                batch_x, batch_y = self.get_train_batch(i, self.train_batch_size)

                # 梯度下降法训练
                _, cost_ = sess.run([optimizer, cost], feed_dict={self.X: batch_x, self.Y: batch_y, self.keep_prob: 0.75})

                if step % 10 == 0:  # 每10 step计算一次准确率
                    # 计算精度
                    batch_x_t, batch_y_t = self.get_verify_batch(64)
                    acc_char = sess.run(accuracy, feed_dict={self.X: batch_x_t, self.Y: batch_y_t, self.keep_prob: 1.})
                    acc_img = sess.run(accuracy_image_count, feed_dict={self.X: batch_x_t, self.Y: batch_y_t, self.keep_prob:1.})

                    print ("Iter:{0}, Minibatch Loss= {1}，".format(step, cost_) +
                           "Accuracy_char= {:.5f}，Accuracy_img = {:.5f}".format(acc_char, acc_img))
                    if acc_img > self.acc_stop:
                        saver.save(sess, self.model_save_dir)
                        print("准确率得到标准，保存模型")
                        break

                    if step % 500 == 0:
                        saver.save(sess, self.model_save_dir)
                        print('保存模型：{}'.format(step))
                step += 1
            saver.save(sess, self.model_save_dir)

            print ("Optimization Finished!")
            # 计算测试精度
            batch_x_t, batch_y_t = self.get_verify_batch(128)
            print( "Testing Accuracy:",step, sess.run(accuracy, feed_dict={self.X: batch_x_t, self.Y: batch_y_t, self.keep_prob: 1.}))


def main():
    with open("conf/config.json", 'r') as f:
        conf = json.load(f)
    train_image_dir = conf["train_image_dir"]
    verify_image_dir = conf["test_image_dir"]
    model_save_dir = conf["model_save_dir"]
    cycle_stop = conf["cycle_stop"]
    acc_stop = conf["acc_stop"]
    cycle_save = conf["cycle_save"]
    enable_gpu = conf["enable_gpu"]
    train_batch_size = conf['train_batch_size']
    test_batch_size = conf['test_batch_size']
    char_set = conf['char_set']

    if not enable_gpu:
        # 设置以下环境变量可开启CPU识别
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    tm = train_model(train_image_dir, verify_image_dir, char_set, model_save_dir, cycle_stop, acc_stop, cycle_save,
                    train_batch_size, test_batch_size)
    tm.train()  # 开始训练模型
    # tm.recognize_captcha()  # 识别图片示例


if __name__ == '__main__':
    main()