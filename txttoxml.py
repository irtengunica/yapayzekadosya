import xml.etree.ElementTree as ET
import glob
import os
import random
import time
import cv2
kaynakklasor='train_detect/labels/'
hedefklasor='train_detect/labels/'
resimklasör='train_detect/images/'
dosyalistesi=list(glob.glob(kaynakklasor+'*.txt'))
dosyasayisi=len(dosyalistesi)-1
for file in list(glob.glob(kaynakklasor+"*.txt")):
 #print(file)
 #print(dosyasayisi)
 #secilendosyano=random.randint (1,dosyasayisi)
 secilendosya=dosyalistesi[dosyasayisi]
 dosyaAdi = secilendosya.replace(kaynakklasor, "")
 #dosyaAdi = dosyaAdi.replace(".jpg", "")
 dosyaAdi = dosyaAdi.replace(".txt", "")
 resimadi=dosyaAdi+".jpg"
 xmladi=dosyaAdi+".xml"
 #print(dosyaAdi)
 print(resimadi)
 #print(xmladi)
 dosyasayisi=dosyasayisi-1
 img = cv2.imread(resimklasör+resimadi)
 height, width, channels = img.shape
 #print(height, width, channels)
 annotation = ET.Element("annotation")
 ET.SubElement(annotation, "folder").text = "train"
 ET.SubElement(annotation, "filename").text = str(resimadi)
 ET.SubElement(annotation, "path").text = str(resimklasör+resimadi)
 source = ET.SubElement(annotation, "source")
 ET.SubElement(source, "database").text = "Unknown"
 size = ET.SubElement(annotation, "size")
 ET.SubElement(size, "width").text = str(width)
 ET.SubElement(size, "height").text = str(height)
 ET.SubElement(size, "depth").text = str(channels)
 ET.SubElement(annotation, "segmented").text = "0"
 fihrist = open(kaynakklasor+dosyaAdi+".txt")
 satir1=fihrist.readlines()
 #print(satir1)
 for line in satir1:
  Type = line.split()
  nesneadi = Type[0]
  x1 = Type[4]
  y1 = Type[5]
  x2 = Type[6]
  y2 = Type[7]
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
 tree.write("train/"+dosyaAdi+".xml")


