import xml.etree.ElementTree as ET
import glob
import os
import random
import time
kaynakklasor='detecnet_data/train_detect/labels/'
hedefklasor='detecnet_data/train_detect/labels/'
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
 print(dosyaAdi)
 print(resimadi)
 print(xmladi)
 dosyasayisi=dosyasayisi-1
fihrist = open(kaynakklasor+"deneme"+".txt")
satir1=fihrist.readlines()
print(satir1)
for line in satir1:
 Type = line.split()
 nesneadi = Type[0]
 x1 = Type[4]
 y1 = Type[5]
 x2 = Type[6]
 y2 = Type[7]
 print(nesneadi,x1,y1,x2,y2)

#satir1 = satir1.split()
#satir1=satir1.split()

#print(satir1[0])
 #hedefdosya=secilendosya.replace(kaynakklasor, hedefklasor)
# os.rename(kaynakklasor+dosyaAdi+".jpg",hedefklasor+"image"+str(i)+".jpg")
# os.rename(kaynakklasor+dosyaAdi+".txt",hedefklasor+"image"+str(i)+".txt")
# os.rename(kaynakklasor+dosyaAdi+".jpg",hedefklasor+"images/a"+dosyaAdi+".jpg")
# os.rename(kaynakklasor+dosyaAdi+".txt",hedefklasor+"labels/a"+dosyaAdi+".txt")
# time.sleep(1)
#os.remove(kaynakklasor+dosyaAdi+".jpg")
#os.remove(kaynakklasor+dosyaAdi+".txt")
