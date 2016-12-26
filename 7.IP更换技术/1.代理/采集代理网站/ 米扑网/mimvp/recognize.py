#coding:utf-8

import os
import requests
from PIL import Image
import math

def imagesget():
    os.mkdir('images')
    count=0
    while True:
        img=requests.get('http://wsxk.hust.edu.cn/randomImage.action').content
        with open('images/%s.jpeg'%count,'wb') as imgfile:
            imgfile.write(img)
        count+=1
        if(count==100):
            break

def convert_image(image):
    image=image.convert('L')
    image2=Image.new('L',image.size,255)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix=image.getpixel((x,y))
            if pix<120:
                image2.putpixel((x,y),0)
    return image2

def cut_image(image):
    inletter=False
    foundletter=False
    letters=[]
    start=0
    end=0
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix=image.getpixel((x,y))
            if(pix==0):
                inletter=True
        if foundletter==False and inletter ==True:
            foundletter=True
            start=x
        if foundletter==True and inletter==False:
            end=x
            letters.append((start,end))
            foundletter=False
        inletter=False
    images=[]
    for letter in letters:
        img=image.crop((letter[0],0,letter[1],image.size[1]))
        images.append(img)
    return images

def buildvector(image):
    result={}
    count=0
    for i in image.getdata():
        result[count]=i
        count+=1
    return result


class CaptchaRecognize:
    def __init__(self):
        self.letters=['0','1','2','3','4','5','6','7','8','9']
        self.loadSet()

    def loadSet(self):
        self.imgset=[]
        for letter in self.letters:
            temp=[]
            for img in os.listdir('mimvp/icon/%s'%(letter)):
                temp.append(buildvector(Image.open('mimvp/icon/%s/%s'%(letter,img))))
            self.imgset.append({letter:temp})

    #计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    #计算矢量之间的 cos 值
    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

    def recognise(self,image):
        image=convert_image(image)
        self.images=cut_image(image)
        vectors=[]
        for img in self.images:
            vectors.append(buildvector(img))
        result=[]
        for vector in vectors:
            guess=[]
            for image in self.imgset:
                for letter,temp in image.items():
                    relevance=0
                    num=0
                    for img in temp:
                        relevance+=self.relation(vector,img)
                        num+=1
                    relevance=relevance/num
                    guess.append((relevance,letter))
            guess.sort(reverse=True)
            result.append(guess[0])
        return result

if __name__=='__main__':
    imageRecognize=CaptchaRecognize()
    count=0
    for imgfile in os.listdir('images'):
        image=Image.open('images/'+imgfile)
        result=imageRecognize.recognise(image)
        images=imageRecognize.images
        for index in range(len(result)):
            try:
                os.mkdir('result/'+result[index][1])
            except:
                pass
            images[index].save('result/'+result[index][1]+'/'+str(count)+'.jpg')
            count+=1
    '''
    count=0
    for imgfile in os.listdir('img'):
        image=Image.open('img/'+imgfile)
        image=convert_image(image)
        images=cut_image(image)
        for img in images:
            img.save('icon/%s.jpg'%count)
            count+=1
    '''
