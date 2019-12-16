import xml.etree.ElementTree as ET
import glob
import os
import random
import time
kaynakklasor='1/'
hedefklasor='detecnet_data/val_detect/'
for i in range(1,1201):
 dosyalistesi=list(glob.glob(kaynakklasor+'*.*'))
 dosyasayisi=len(dosyalistesi)
 print(dosyasayisi)
 secilendosyano=random.randint (1,dosyasayisi)
 secilendosya=dosyalistesi[secilendosyano]
 dosyaAdi = secilendosya.replace(kaynakklasor, "")
 dosyaAdi = dosyaAdi.replace(".jpg", "")
 dosyaAdi = dosyaAdi.replace(".txt", "")
 print(dosyaAdi)
 hedefdosya=secilendosya.replace(kaynakklasor, hedefklasor)
# os.rename(kaynakklasor+dosyaAdi+".jpg",hedefklasor+"image"+str(i)+".jpg")
# os.rename(kaynakklasor+dosyaAdi+".txt",hedefklasor+"image"+str(i)+".txt")
 os.rename(kaynakklasor+dosyaAdi+".jpg",hedefklasor+"images/a"+dosyaAdi+".jpg")
 os.rename(kaynakklasor+dosyaAdi+".txt",hedefklasor+"labels/a"+dosyaAdi+".txt")
# time.sleep(1)
#os.remove(kaynakklasor+dosyaAdi+".jpg")
#os.remove(kaynakklasor+dosyaAdi+".txt")
