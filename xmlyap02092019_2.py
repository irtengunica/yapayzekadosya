#!/usr/bin/python

import xml.etree.ElementTree as ET
import argparse
import sys
import glob
import os
import numpy as np
import cv2
import json 
import urllib.request
import random


#engin
with open("response1.json") as json_file1:
 dosyalistesi=json.load(json_file1)
dosyasayisi= len(dosyalistesi)-1
#print(dosyalistesi)
#print(dosyasayisi)
frame_idlist=[]
secilendosyalist=[]
#resimadilist=[]
for item in dosyalistesi:
 frame_idlist=frame_idlist+[(item['frame_id'])]
 secilendosya=item['frame_link']
 dosyaAdi = secilendosya.replace("http://212.68.57.202/images/", "")
 dosyaAdi5 = dosyaAdi.replace("B23072019_V1_K1/", "")
 dosyaAdi5 = dosyaAdi.replace("T190619_V4_K1/", "")
 #resimadi = dosyaAdi5.replace(".jpg", "")
 resimadi = dosyaAdi5
 secilendosyalist=secilendosyalist+[dosyaAdi]
 #resimadilist=resimadilist+[resimadi]
 #dosyasayisi=dosyasayisi-1
#print(secilendosyalist,frame_idlist)
#print((frame_idlist))
dx=0
with open("testtf1.json") as json_file:  
 data = json.load(json_file)
 for jsn in data['frameler']:
  print(frame_idlist[dx],jsn['frame_id'],secilendosyalist[jsn['frame_id']-1])
  if frame_idlist[dx]==jsn['frame_id']:
   img = cv2.imread(secilendosyalist[jsn['frame_id']-1])
   height, width, channels = img.shape
   ydosyaadi='image'+str(random.randint (0,6000))+str(dx)+'.jpg'
   yklasor='train'
   yklasoryol=yklasor+'/'+ydosyaadi
   annotation = ET.Element("annotation")
   ET.SubElement(annotation, "folder").text = yklasor
   ET.SubElement(annotation, "filename").text = ydosyaadi
   ET.SubElement(annotation, "path").text = yklasoryol
   source = ET.SubElement(annotation, "source")
   ET.SubElement(source, "database").text = "Unknown"
   size = ET.SubElement(annotation, "size")
   ET.SubElement(size, "width").text = str(width)
   ET.SubElement(size, "height").text = str(height)
   ET.SubElement(size, "depth").text = str(channels)
   ET.SubElement(annotation, "segmented").text = "0"
   objs = jsn['objeler']
   for o in objs:
    if(o['tur'] == 'yaya'or o['tur'] == 'arac'):
     nesneadi=o['tur']
     x1 = o['x1']
     y1 = o['y1']
     x2 = o['x2']
     y2 = o['y2']
     object = ET.SubElement(annotation, "object")
     ET.SubElement(object, "name").text = str(nesneadi)
     ET.SubElement(object, "pose").text = "Unspecified"
     ET.SubElement(object, "truncated").text = "0"
     ET.SubElement(object, "difficult").text = "0"
     bndbox = ET.SubElement(object, "bndbox")
     ET.SubElement(bndbox, "xmin").text = str(x1)
     ET.SubElement(bndbox, "ymin").text = str(y1)
     ET.SubElement(bndbox, "xmax").text = str(x2)
     ET.SubElement(bndbox, "ymax").text = str(y2)
   tree = ET.ElementTree(annotation)
    #tree.write("train/"+dosyaAdi+".xml",encoding="UTF-8",xml_declaration=True)
   tree.write(yklasoryol.replace('.jpg','')+".xml")
   os.rename(str(secilendosyalist[jsn['frame_id']-1]),yklasoryol)
    #else:
     #color = (255,0,0)
    #cv2.rectangle(image, (int(o['x1']),int(o['y1'])), (int(o['x2']),int(o['y2'])), color, 2)
    #cv2.putText(image1,str(o['x1']),(10,500),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),2)
   #image=cv2.putText(image,secilendosyalist[jsn['frame_id']-1]+'_'+str(jsn['frame_id']),(10,500),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),8,cv2.LINE_AA)
   #image=cv2.resize(image,(800,600))
   #cv2.imshow("Deneme",image)
   #cv2.waitKey(0)
  dx=dx+1