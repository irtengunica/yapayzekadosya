import numpy as np

import cv2
import sys
import json 
import urllib.request
from urllib.request import urlopen
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image
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


