#!/usr/bin/python
import argparse
import sys
import glob
import os
import numpy as np
import cv2
import json 
import urllib.request
import requests
#giris
s = requests.Session()
url = 'http://212.68.57.202:52196/api/giris'
data = {"kadi" : "karaelmas","sifre" : "teknoyz449"}
r = s.post(url, json=data)
print(r.status_code)
get_url = 'http://212.68.57.202:52196/api/cevap_gonder'
#veri yolla deneme
#data ={"frame_id": 9, "objeler": []}
#p = s.post(get_url, json=data)
#print(p.status_code)

#with open("testtf1.json") as json_file:  
 #data = json.load(json_file)
 #p = s.post(get_url, json=data)
 #print(p.status_code)

#tum veriyi yolla
with open("testtf1.json") as json_file:  
 data = json.load(json_file)
 for jsn in data['frameler']:
  print(jsn)
  p = s.post(get_url, json=jsn)
  print(p.status_code)
#cikis
get_url = 'http://212.68.57.202:52196/api/cikis'
p = s.get(get_url)
print(p.status_code)

