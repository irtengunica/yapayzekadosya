# import the necessary packages
#!/usr/bin/env tensorflowenv
import numpy as np
import urllib.request
import cv2
import json 

file_path = 'v.json'
images_path = ''

with open(file_path) as json_file:  
    data = json.load(json_file)
    print(data)
    for jsn in data['frameler']:
    	url = images_path + jsn['frame_url']
    	objs = jsn['objeler']
    	image = cv2.imread(url,cv2.IMREAD_COLOR)
    	for o in objs:
    		if(o['tur'] == 'yaya'):
    			color = (0,0,255)
    		else:
    			color = (255,0,0)
    		cv2.rectangle(image, (int(o['x0']),int(o['y0'])), (int(o['x1']),int(o['y1'])), color, 2)
    	cv2.imshow("Deneme",image)
    	cv2.waitKey(0)



