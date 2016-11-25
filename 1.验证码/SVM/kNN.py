#coding:utf-8
#!/usr/bin/python

from numpy import *
import operator
from os import listdir
import matplotlib.pyplot as plt 
from sklearn import datasets, svm, metrics

clf = svm.SVC()


def classify0(inX, dataSet, labels, k):#分别是 测试向量，训练集合，原始数值标记， k值
    dataSetSize = dataSet.shape[0] # 获取测试集合的数量

    #此为计算距离运用python的二维数组的运算，先将测试向量，按照训练集合的行数进行平铺，然后直接二维相减
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2 # 平方
    sqDistances = sqDiffMat.sum(axis=1) # 计算每一行的总和，
    distances = sqDistances**0.5 # 开方
    sortedDistIndicies = distances.argsort() # 索引排序，不会导致排序后找不到原始顺序的问题 array.argsort()，得到每个元素的排序序号

    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # get(key,x)从字典中获取key对应的value，没有key的话返回0
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True) # sorted()函数，按照第二个元素即value的
    return sortedClassCount[0][0]

def img2vector(filename):
    #''' 将该文件中32*32转换为1*1024长的向量，采用首尾链接的方式进行二维转一维 返回的是一维数组'''
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    #trainingFileList = listdir('trainingDigits') # 读取训练集合列表
    trainingFileList = listdir('0') # 读取训练集合列表
    m = len(trainingFileList)
    trainingMat = zeros((m,1024)) # 构建一个m×1024,的数组，值全部为0
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr) # 根据文件名切割取出该训练样板的真实数值
        trainingMat[i,:] = img2vector('0/%s' % fileNameStr)

    testFileList = listdir('testDigits') #获取测试集合

    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr) # 截取测试集合的名字
            
        print vectorUnderTest

        #classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 2) # 进行分类， k值为3
        
        #print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        #if (classifierResult != classNumStr): errorCount += 1.0

    print clf.fit(vectorUnderTest,trainingMat)
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))


if __name__ == '__main__':
    handwritingClassTest()
