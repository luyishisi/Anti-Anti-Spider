#coding:utf-8
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request
import base64
import random
import time

#定义一个flask app
app = Flask(__name__)

number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 图像大小
IMAGE_HEIGHT = 30
IMAGE_WIDTH = 100
MAX_CAPTCHA = 4

# 把彩色图像转为灰度图像（色彩对识别验证码没有什么用）
def convert2gray(img):
	if len(img.shape) > 2:
		gray = np.mean(img, -1)
		# 上面的转法较快，正规转法如下
		# r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
		# gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
		return gray
	else:
		return img

"""
cnn在图像大小是2的倍数时性能最高, 如果你用的图像大小不是2的倍数，可以在图像边缘补无用像素。
np.pad(image【,((2,3),(2,2)), 'constant', constant_values=(255,))  # 在图像上补2行，下补3行，左补2行，右补2行
"""

# 文本转向量
char_set = number + alphabet + ALPHABET + ['_']  # 如果验证码长度小于4, '_'用来补齐
CHAR_SET_LEN = len(char_set)
def text2vec(text):
	text_len = len(text)
	if text_len > MAX_CAPTCHA:
		raise ValueError('验证码最长4个字符')

	vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN) #生成一个默认为0的向量
	def char2pos(c):
		if c =='_':
			k = 62
			return k
		k = ord(c)-48
		if k > 9:
			k = ord(c) - 55
			if k > 35:
				k = ord(c) - 61
				if k > 61:
					raise ValueError('No Map')
		return k
	for i, c in enumerate(text):
		idx = i * CHAR_SET_LEN + char2pos(c)
		vector[idx] = 1
	return vector
# 向量转回文本
def vec2text(vec):
	char_pos = vec.nonzero()[0]
	text=[]
	for i, c in enumerate(char_pos):
		char_at_pos = i #c/63
		char_idx = c % CHAR_SET_LEN
		if char_idx < 10:
			char_code = char_idx + ord('0')
		elif char_idx <36:
			char_code = char_idx - 10 + ord('A')
		elif char_idx < 62:
			char_code = char_idx-  36 + ord('a')
		elif char_idx == 62:
			char_code = ord('_')
		else:
			raise ValueError('error')
		text.append(chr(char_code))
	return "".join(text)

"""
#向量（大小MAX_CAPTCHA*CHAR_SET_LEN）用0,1编码 每63个编码一个字符，这样顺利有，字符也有
vec = text2vec("F5Sd")
text = vec2text(vec)
print(text)  # F5Sd
vec = text2vec("SFd5")
text = vec2text(vec)
print(text)  # SFd5
"""

# 生成一个训练batch
def get_next_batch(batch_size=128):
	batch_x = np.zeros([batch_size, 30*100])
	batch_y = np.zeros([batch_size, MAX_CAPTCHA*CHAR_SET_LEN])

	# 有时生成图像大小不是(60, 160, 3)
	def wrap_gen_captcha_text_and_image():
		''' 获取一张图，判断其是否符合（60，160，3）的规格'''
		while True:
			text, image = gen_captcha_text_and_image()
			#if image.shape == (30, 100, 3):#此部分应该与开头部分图片宽高吻合
			return text, image

	for i in range(batch_size):
		text, image = wrap_gen_captcha_text_and_image()
		# 将图片数组一维化 同时将文本也对应在两个二维组的同一行
		batch_x[i,:] = image / 255 # (image.flatten()-128)/128  mean为0
		batch_y[i,:] = text2vec(text)
	# 返回该训练批次
	return batch_x, batch_y
####################################################################

# 申请三个占位符
X = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT*IMAGE_WIDTH])
Y = tf.placeholder(tf.float32, [None, MAX_CAPTCHA*CHAR_SET_LEN])
keep_prob = tf.placeholder(tf.float32) # dropout

# 定义CNN
def crack_captcha_cnn(w_alpha=0.01, b_alpha=0.1):
	# 将占位符 转换为 按照图片给的新样式
	x = tf.reshape(X, shape=[-1, 30, 100, 1])
	print("reshaped")

	#w_c1_alpha = np.sqrt(2.0/(IMAGE_HEIGHT*IMAGE_WIDTH)) #
	#w_c2_alpha = np.sqrt(2.0/(3*3*32))
	#w_c3_alpha = np.sqrt(2.0/(3*3*64))
	#w_d1_alpha = np.sqrt(2.0/(8*32*64))
	#out_alpha = np.sqrt(2.0/1024)

	# 3 conv layer
	w_c1 = tf.Variable(w_alpha*tf.random_normal([3, 3, 1, 32])) # 从正太分布输出随机值
	b_c1 = tf.Variable(b_alpha*tf.random_normal([32]))
	conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, w_c1, strides=[1, 1, 1, 1], padding='SAME'), b_c1))
	conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
	conv1 = tf.nn.dropout(conv1, keep_prob)

	w_c2 = tf.Variable(w_alpha*tf.random_normal([3, 3, 32, 64]))
	b_c2 = tf.Variable(b_alpha*tf.random_normal([64]))
	conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1, w_c2, strides=[1, 1, 1, 1], padding='SAME'), b_c2))
	conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
	conv2 = tf.nn.dropout(conv2, keep_prob)

	w_c3 = tf.Variable(w_alpha*tf.random_normal([3, 3, 64, 64]))
	b_c3 = tf.Variable(b_alpha*tf.random_normal([64]))
	conv3 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv2, w_c3, strides=[1, 1, 1, 1], padding='SAME'), b_c3))
	conv3 = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
	conv3 = tf.nn.dropout(conv3, keep_prob)

	# Fully connected layer
	w_d = tf.Variable(w_alpha*tf.random_normal([4*13*64, 1024]))
	b_d = tf.Variable(b_alpha*tf.random_normal([1024]))
	dense = tf.reshape(conv3, [-1, w_d.get_shape().as_list()[0]])
	dense = tf.nn.relu(tf.add(tf.matmul(dense, w_d), b_d))
	dense = tf.nn.dropout(dense, keep_prob)

	w_out = tf.Variable(w_alpha*tf.random_normal([1024, MAX_CAPTCHA*CHAR_SET_LEN]))
	b_out = tf.Variable(b_alpha*tf.random_normal([MAX_CAPTCHA*CHAR_SET_LEN]))
	out = tf.add(tf.matmul(dense, w_out), b_out)
	#out = tf.nn.softmax(out)
	return out

output = crack_captcha_cnn()

saver = tf.train.Saver()
sess = tf.Session()
saver.restore(sess, tf.train.latest_checkpoint('.'))

predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
def crack(captcha_image):
	text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})

	text = text_list[0].tolist()
	vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN)
	i = 0
	for n in text:
			vector[i*CHAR_SET_LEN + n] = 1
			i += 1
	return vec2text(vector)


@app.route('/api')
def fun():
	b = request.args.get("b64")
	path = "./temp/" + str(time.time()) + "_" + str(random.random()) + ".jpg"
	open(path,'wb').write(base64.b64decode(b.encode()))
	captcha_image = Image.open(path)
	captcha_image = np.array(captcha_image)
	captcha_image = convert2gray(captcha_image)
	captcha_image = captcha_image.flatten() / 255 # 将图片一维化
	predict_text = crack(captcha_image)
	print(predict_text)
	return predict_text

if __name__ == '__main__':
	app.run()

	#train_crack_captcha_cnn()
