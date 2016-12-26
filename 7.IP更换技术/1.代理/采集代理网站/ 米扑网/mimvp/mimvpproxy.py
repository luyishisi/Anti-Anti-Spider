import requests
from bs4 import BeautifulSoup
import mimvp.recognize
from PIL import Image
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

def mimvp_proxy():
    urls=['http://proxy.mimvp.com/free.php?proxy=in_tp','http://proxy.mimvp.com/free.php?proxy=in_hp']
    for url in urls:
        html=requests.get(url,headers=headers).text
        table=BeautifulSoup(html,'lxml').find('div',id='list').find('tbody')#.find_all('tr')
        table=re.findall('(\d+\.\d+\.\d+\.\d+).*?img src="(.*?)"',str(table))
        imageRecognize=mimvp.recognize.CaptchaRecognize()
        iplist=[]
        for item in table:
            try:
                ip=item[0]
                imgurl='http://proxy.mimvp.com/'+item[1].replace('amp;','')
                image=getimage(imgurl)
                result=imageRecognize.recognise(image)
                port=[item[1] for item in result]
                port=''.join(port)
                print(ip+':'+port)
                iplist.append(ip+':'+port)
            except:
                continue
    return iplist

def getimage(imgurl):
    with open('mimvp/temp.png','wb') as img:
        content=requests.get(imgurl,headers=headers).content
        img.write(content)
    image=Image.open('mimvp/temp.png')
    image=mimvp.recognize.convert_image(image)
    return image
