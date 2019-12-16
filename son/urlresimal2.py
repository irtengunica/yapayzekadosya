import numpy as np
import urllib
import cv2
import sys
import json 
import urllib.request
from skimage import io

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
 #dosyaAdi = secilendosya.replace("http://212.68.57.202/images/", "")
 #dosyaAdi = dosyaAdi.replace("B23072019_V1_K1/", "")
 #dosyaAdi = dosyaAdi.replace("T190619_V4_K1/", "")
 #resimadi = dosyaAdi.replace(".jpg", "")
 #urllib.request.urlretrieve(secilendosya, kaynakklasor+dosyaAdi)
 secilendosyalist=secilendosyalist+[secilendosya]
 #dosyasayisi=dosyasayisi-1
 image = url_to_image(secilendosya)
 cv2.imshow("Image", image)
 cv2.waitKey(0)
 print(secilendosya)
print(len(secilendosyalist))
print(len(frame_idlist))


