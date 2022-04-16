import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import sys
import json
import argparse

from PIL import Image

# Argument definition

parser = argparse.ArgumentParser(description = "Predict which class a flower in an image belongs to")
parser.add_argument('-i', '--image_path', default = "./test_images/hard-leaved_pocket_orchid.jpg", help = 'Image path')
parser.add_argument('-m', '--checkpoint', help = "Model checkpoint")
parser.add_argument('-k', '--top_k', default = 5, type = int, help = "Top K most likely classes")
parser.add_argument('-c', '--category_names', default = 'label_map.json', help = "Maps the real categories name")
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

if __name__ == '__main__':
    probs, classes = predict(image_path, model, 5)
    print(probs)
    print(classes)
