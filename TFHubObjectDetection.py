import tensorflow as tf
import tensorflow_hub as hub

from Dataset import Dataset
dataset = Dataset()

module = hub.Module('https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1')
detector = module(dict(images=dataset.image_data), as_dict=True)

class_entities = detector['detection_class_entities']
boxes = detector['detection_boxes']
scores = detector['detection_scores']
class_labels = detector['detection_class_labels']
class_names = detector['detection_class_names']