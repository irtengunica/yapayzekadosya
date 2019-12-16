#!/usr/bin/python


import argparse
import sys
import glob
import os
import numpy as np
import cv2
import json 
import urllib.request
from urllib.request import urlopen

#engin
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

with open("response1.json") as json_file1:
 dosyalistesi=json.load(json_file1)
dosyasayisi= len(dosyalistesi)-1
hedefklasor='gir/'
frame_idlist=[]
secilendosyalist=[]
for item in dosyalistesi:
 frame_idlist=frame_idlist+[(item['frame_id'])]
 secilendosya=item['frame_link']
 #dosyaAdi = secilendosya.replace("http://212.68.57.202/images/", "")
 #dosyaAdi = dosyaAdi.replace("B23072019_V1_K1/", "")
 #dosyaAdi = dosyaAdi.replace("T190619_V4_K1/", "")
 #resimadi = dosyaAdi.replace(".jpg", "")
 secilendosyalist=secilendosyalist+[secilendosya]
 #dosyasayisi=dosyasayisi-1
print(len(secilendosyalist))
print(len(frame_idlist))
dx=0
with open("test201.json") as json_file:  
 data = json.load(json_file)
 for jsn in data['frameler']:
  print(frame_idlist[dx],jsn['frame_id'],secilendosyalist[(jsn['frame_id'])-1])
  if frame_idlist[dx]==jsn['frame_id']:
   url = secilendosyalist[jsn['frame_id']-1]
   print(url)
   objs = jsn['objeler']
   image = url_to_image(url)
   #image = cv2.imread(url,cv2.IMREAD_COLOR)
   for o in objs:
    if(o['tur'] == 'yaya'):
     color = (0,0,255)
    else:
     color = (255,0,0)
    cv2.rectangle(image, (int(o['x1']),int(o['y1'])), (int(o['x2']),int(o['y2'])), color, 2)
    #cv2.putText(image1,str(o['x1']),(10,500),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),2)
   image=cv2.putText(image,secilendosyalist[jsn['frame_id']-1]+'_'+str(jsn['frame_id']),(10,500),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),8,cv2.LINE_AA)
   image=cv2.resize(image,(800,600))
   cv2.imshow("Deneme",image)
   cv2.waitKey(0)
  dx=dx+1
