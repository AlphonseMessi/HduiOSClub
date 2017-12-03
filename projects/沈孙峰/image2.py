
import requests
from bs4 import BeautifulSoup
import os

j=0
def get_image(html):
 global j
 urls = BeautifulSoup(html,"lxml")
 images = urls.find_all("img",class_="gitem")
 for image in images:
     img_content = requests.get(image['src']).content
     with open("img{}.jpg".format(j),'wb')  as a:
        a.write(img_content)
        j = j + 1
  
for i in range(0,3):
    html=requests.get("http://www.meizit.com/home/index/index?t=气质&p={}".format(i)).text
    get_image(html)
