import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import sys
import json
import argparse

from PIL import Image

# Argument definition

parser = argparse.ArgumentParser(description = "Predict which class a flower in an image belongs to")
parser.add_argument('image_path', type=str, default = "./test_images/hard-leaved_pocket_orchid.jpg", help = 'Image path')
parser.add_argument('checkpoint', type=str, help = "Model checkpoint path")
parser.add_argument('-k', '--top_k', default = 5, type = int, help = "Top K most likely classes")
parser.add_argument('-n', '--category_names', type=str, default = 'label_map.json', help = "Maps the real categories name")
args = parser.parse_args()

# Argument assignment

image_path = args.image_path
model_checkpoint =  args.checkpoint
top_k = args.top_k
label_map = args.category_names

# Mapping from label to category name
with open(label_map, 'r') as f:
    class_names = json.load(f)

# Load the Keras Model
model = tf.keras.models.load_model(model_checkpoint,
                                   custom_objects={'KerasLayer':hub.KerasLayer})

# Preprocessing image function                    
def process_image (image):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image /= 255
    return image

# Predict image function 
def predict(image_path, model, top_k = top_k):
    
    im = Image.open(image_path)
    image = np.asarray(im)
    processed_image = process_image(image)
    
    prediction = model.predict(np.expand_dims(processed_image, axis=0))
    probs, classes = tf.math.top_k(prediction, k = top_k)


    return probs.numpy()[0], classes.numpy()[0]

# model inference
probs, classes = predict(image_path, model, top_k)

# Model results
top_classes = [str(cls) for cls in classes]
top_classes_names = [class_names[top_class] for top_class in top_classes]

# Results presentation
print("\n")
print("--------------------Prediction Results------------------")
print("The top {} probabilities are :".format(top_k))
print(probs)
print("The top {} classes are :".format(top_k))
print(top_classes_names)
print("\n")
