import xml.etree.ElementTree as ET
import glob
import os
import random
import time
kaynakklasor='1/'
hedefklasor='2/'
for i in range(1,2000):
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
 os.rename(kaynakklasor+dosyaAdi+".jpg",hedefklasor+"a"+dosyaAdi+".jpg")
 os.rename(kaynakklasor+dosyaAdi+".txt",hedefklasor+"a"+dosyaAdi+".txt")
# time.sleep(1)
#os.remove(kaynakklasor+dosyaAdi+".jpg")
#os.remove(kaynakklasor+dosyaAdi+".txt")
