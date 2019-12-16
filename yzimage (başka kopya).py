######## Image Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Date: 1/15/18
# Description: 
# This program uses a TensorFlow-trained classifier to perform object detection.
# It loads the classifier uses it to perform object detection on an image.
# It draws boxes and scores around the objects of interest in the image.

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

## but I changed it to make it more understandable to me.

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import json 
import urllib.request
import glob
from urllib.request import urlopen

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'karaelmas'
IMAGE_NAME = 'resimler/f6.jpg'

#siniflar
class Cerceve(object):
    def __init__(self, frame_id):
        self.frame_id = frame_id
        self.objeler =""


    # This method can return a python dict object by the class instance.
    # And the dict object can be serialized to JSON.
    def cerceve2dict(self, cerceveadi):
        return {
            'frame_id': cerceveadi.frame_id,
            'objeler':	altcerceve
        }
class AltCerceve(object):
    
    def __init__(self, tur, x1, y1, x2, y2):
    
        self.tur = tur
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def toJson(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)   
#siniflar
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
 ##image = url_to_image(secilendosya)
 ##cv2.imshow("Image", image)
 ##cv2.waitKey(0)
 print(secilendosya)
print(len(secilendosyalist))
print(len(frame_idlist))

for item in frame_idlist:
 frame_id=frame_idlist[item-1]
 frame_link=secilendosyalist[item-1]
 secilendosya=frame_link
 dosyaAdi = secilendosya.replace("B23072019_V1_K1/", "")
 dosyaAdi = dosyaAdi.replace("T190619_V4_K1/", "")
 resimadi = dosyaAdi.replace(".jpg", "")
 secilendosya=kaynakklasor+frame_link
 hedefdosya=hedefklasor+frame_link
 #print(dosyaAdi)
 #print(resimadi)
 #dosyasayisi=dosyasayisi-1
 #img2 = cv2.imread(secilendosya)
 #height, width, channels = img2.shape
 #kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
 #img3 = cv2.filter2D(img2, -1, kernel_sharpen_1) 
 #print(height, width, channels)
#engin
# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'karaelmas.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_NAME,'karaelmas.pbtxt')

# Path to image
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

# Number of classes the object detector can identify
NUM_CLASSES = 2

# Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Load image using OpenCV and
# expand image dimensions to have shape: [1, None, None, 3]
# i.e. a single-column array, where each item in the column has the pixel RGB value
image = cv2.imread(PATH_TO_IMAGE)
height, width, channels = image.shape
image_expanded = np.expand_dims(image, axis=0)

# Perform the actual detection by running the model with the image as input
(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})
# Draw the results of the detection (aka 'visulaize the results')

vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=5,
    min_score_thresh=0.60)
boxes1=np.squeeze(boxes)
classes1=np.squeeze(classes).astype(np.int32)
scores1=np.squeeze(scores)
min_score_thresh=0.60
max_boxes_to_draw = boxes1.shape[0]
altcerceve = []
for i in range(min(max_boxes_to_draw, boxes1.shape[0])):
 if scores1 is None or scores1[i] > min_score_thresh:
   box = tuple(boxes1[i].tolist())
   print(box)
   ymin, xmin, ymax, xmax = box
   y1 = int(ymin*height)
   x1 = int(xmin*width)
   y2 = int(ymax*height)
   x2 = int(xmax*width)
#  print('??????')
   print(x1,y1,x2,y2)
   if classes1[i] in category_index.keys():
     class_name = category_index[classes1[i]]['name']
   else:
     class_name = 'N/A'
   print(class_name)
   p1 = AltCerceve(class_name,x1,y1,x2,y2)
   altcerceve.append(json.loads(p1.toJson()))
cerceveadi =Cerceve(1)# Cerceve(frame_id)
if os.path.isfile("karaelmas/test200.json"):
 with open('karaelmas/test200.json', 'a') as f:
  f.write(json.dumps(cerceveadi, default=cerceveadi.cerceve2dict))
  f.write('\n ')
else:
 with open('karaelmas/test200.json', 'w') as f:
  f.write(json.dumps(cerceveadi, default=cerceveadi.cerceve2dict))
  f.write('\n ')
# All the results have been drawn on image. Now display the image.
image=cv2.resize(image,(800,600))
cv2.imshow('Object detector', image)

# Press any key to close the image
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()
