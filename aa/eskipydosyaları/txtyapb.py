# import the necessary packages
#!/usr/bin/env tensorflowenv
import numpy as np
import urllib.request
#import cv2
import json 
import os

file_path = 'T190619_V5_K1_p2_s500'
dir__ = 'T190619_V5_K1'
images_path = ''

with open(file_path) as json_file:  
    data = json.load(json_file)
#    print(data)
    for jsn in data['data']:
    	dosyaAdi = images_path + jsn['frame_link']
    	dosyaAdi5 = dosyaAdi.replace(dir__, "")
    	dosyaAdi4 = dosyaAdi5.replace("/", "")
    	dosyaAdi3 = dosyaAdi4.replace(".jpg", "")
    	print(dosyaAdi3)
    	dosya = open('./'+dir__+'/txt/b'+dosyaAdi3+'.txt', 'a+')
    	os.rename(dosyaAdi,'./'+dir__+'/b'+dosyaAdi4)
    	objs = jsn['objeler']
    	for o in objs:
         if(o['tur'] == 'yaya' or o['tur'] == 'arac'):
          xmin=str(int(o['x1']))
          ymin=str(int(o['y1']))
          xmax=str(int(o['x2']))
          ymax=str(int(o['y2']))
          icerik = o['tur'] + ' ' + '0 0 0 ' + xmin + ' ' + ymin + ' ' + xmax + ' ' + ymax + ' 0 0 0 0 0 0 0\n'
          dosya.write(icerik)


