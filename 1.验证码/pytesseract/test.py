#coding:utf-8
import urllib
from cStringIO import StringIO
from PIL import Image
import re,os,sys
import pytesseract

def url_to_image_date(url):
    data = None
    try:
        stream = urllib.urlopen(url)
        data = stream.read()
    finally:
        stream.close()
    return data

def image_data_to_tiff(data):
    img = Image.open(StringIO(data))
    img = img.convert('RGBA') #类型转换
    img = binarize_image(img)#二值化
    img = img.convert('L')
    return img

def binarize_image(img):
    pixdata = img.load()
    print img.size[1]
    print img.size[0]
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x,y][0] < 100 or pixdata[x,y][1] < 100 or  pixdata[x,y][2] < 100:
                pixdata[x,y] = (0,0,0,255)
            else:
                pixdata[x,y] = (255,255,255,255)
    return img

def image_to_text(img):
    return tesseract(img)

def tesseract(img):
    text = pytesseract.image_to_string(img)
    text = re.sub('[\W]', '', text) #将所有【\W】消除
    return text

def test(url,di_name):
    if not os.path.exists(di_name):
        os.mkdir(di_name)
    os.chdir(di_name)

    html = open('result.html','w')
    html.write('<html><body><ul>')

    for i in range(0,100):
        filename = str(i)+'.gif'
        data = url_to_image_date(url)
        img_file = open(filename,'w')
        img_file.write(data)
        img = image_data_to_tiff(data)
        img.convert('RGBA').save('bin_' + filename)
        text = image_to_text(img)
        print text
        html.write('<li>')
        html.write('<img src="'+ filename + '">')
        html.write('<img src="bin_'+ filename + '">')
        html.write('<span>'+ text + '</span>')

        html.write('</li>')
    html.write('</ul></body></html>')
    html.flush()
    html.close()

def parse_captcha(url,filename):
    data = url_to_image_date(url)
    img_file = open(filename,'w')
    img_file.write(data)
    img = image_data_to_tiff(data)
    text = image_to_text(img)
    return text

if __name__ == '__main__':
    url = sys.argv[1]
    di_name = sys.argv[2]
    test(url,di_name)
