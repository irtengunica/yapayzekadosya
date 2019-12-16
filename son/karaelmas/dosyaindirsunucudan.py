import os
import cv2
import numpy as np

import sys
import json 
import urllib.request
import glob

with open("karaelmas/response1.json") as json_file:
 dosyalistesi=json.load(json_file)
#dosyasayisi= len(dosyalistesi)-1
hedefklasor='karaelmas/cik/'
kaynakklasor='karaelmas/gir/'
frame_idlist=[]
secilendosyalist=[]
for item in dosyalistesi:
 frame_idlist=frame_idlist+[(item['frame_id'])]
 secilendosya=item['frame_link']
 dosyaAdi = secilendosya.replace("http://212.68.57.202/images/", "")
 dosyaAdi = dosyaAdi.replace("B23072019_V1_K1/", "")
 dosyaAdi = dosyaAdi.replace("T190619_V4_K1/", "")
 resimadi = dosyaAdi.replace(".jpg", "")
 urllib.request.urlretrieve(secilendosya, kaynakklasor+dosyaAdi)
 secilendosyalist=secilendosyalist+[dosyaAdi]
 #dosyasayisi=dosyasayisi-1
#print(len(secilendosyalist))
#print(len(frame_idlist))

for item in frame_idlist:
 frame_id=frame_idlist[item-1]
 frame_link=secilendosyalist[item-1]
 secilendosya=frame_link
 dosyaAdi = secilendosya.replace("B23072019_V1_K1/", "")
 dosyaAdi = dosyaAdi.replace("T190619_V4_K1/", "")
 resimadi = dosyaAdi.replace(".jpg", "")
 secilendosya=kaynakklasor+frame_link
 hedefdosya=hedefklasor+frame_link
 #print(dosyaAdi)
 #print(resimadi)
 #dosyasayisi=dosyasayisi-1
 #img2 = cv2.imread(secilendosya)
 #height, width, channels = img2.shape
 #kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
 #img3 = cv2.filter2D(img2, -1, kernel_sharpen_1) 
 #print(height, width, channels)
#engin
