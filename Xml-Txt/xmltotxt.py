import xml.etree.ElementTree as ET
import glob
import os

for file in list(glob.glob("xml/*.xml")):
	root = ET.parse(file).getroot()
	for object in root.iter('object'):
		print (object.text)
		for name in object.findall("name"):
			tur = name.text
		for xmin in object.findall("bndbox/xmin"):
			xmin = xmin.text
		for ymin in object.findall("bndbox/ymin"):
			ymin = ymin.text
		for xmax in object.findall("bndbox/xmax"):
			xmax = xmax.text
		for ymax in object.findall("bndbox/ymax"):
			ymax = ymax.text	
		dosyaAdi = file.replace("xml/", "")
		dosyaAdi2 = dosyaAdi.replace(".xml", "")
		dosya = open('./txt/'+dosyaAdi2+'.txt', 'a+')
		icerik = tur + ' ' + '0 0 0 ' + xmin + ' ' + ymin + ' ' + xmax + ' ' + ymax + ' 0 0 0 0 0 0 \n'
		dosya.write(icerik)

print ("Developed by AhmetTuylu !DONE!")
