import pandas as pd
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time
import matplotlib.pyplot as plt
import cv2
import seaborn as sns
sns.set_style('darkgrid')
import shutil
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization
from keras.optimizers import Adam, Adamax
from keras.metrics import categorical_crossentropy
from keras import regularizers
from keras.models import Model
from keras import backend as K



# load the model
#model = VGG16()
def make_model(img_size, lr, mod_num=7):  
    img_shape=(img_size[0], img_size[1], 3)
    if mod_num == 0:
        base_model=keras.applications.efficientnet.EfficientNetB0(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
        msg='Created EfficientNet B0 model'
    elif mod_num == 3:
        base_model=keras.applications.efficientnet.EfficientNetB3(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
        msg='Created EfficientNet B3 model'
    elif mod_num == 5:
        base_model=keras.applications.efficientnet.EfficientNetB5(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max') 
        msg='Created EfficientNet B5 model'
        
    else:
        base_model=keras.applications.efficientnet.EfficientNetB7(include_top=False, weights="imagenet",input_shape=img_shape, pooling='max')
        msg='Created EfficientNet B7 model'   
   
    base_model.trainable=True
    x=base_model.output
    x=BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001 )(x) # 
    x = Dense(256, kernel_regularizer = regularizers.l2(l = 0.016),activity_regularizer=regularizers.l1(0.006),
                    bias_regularizer=regularizers.l1(0.006) ,activation='relu')(x)
    x=Dropout(rate=.4, seed=123)(x)       
    output=Dense(4, activation='softmax')(x)
    model=Model(inputs=base_model.input, outputs=output)
    model.compile(Adamax(learning_rate=lr), loss='categorical_crossentropy', metrics=['accuracy']) 
    msg=msg + f' with initial learning rate set to {lr}'
    print(msg)
    return model

img_size=(93,93) # size of augmented images
lr=.001
model=make_model(img_size, lr) # using B3 model by default



model.load_weights(r'C:\Users\tgillard\Desktop\internship\0_Final_Code\1_Braeburn\Braeburn_tesy.h5')
#summarize the model

import numpy as np
import random

# Get list of layers from model
layer_outputs = [layer.output for layer in model.layers[1:]]
# Create a visualization model
visualize_model = tf.keras.models.Model(inputs = model.input, outputs = layer_outputs)

img = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T2 Eve_trie\Team\train\1stem\9921110.BMP'

img = tf.keras.utils.load_img(
            img, target_size=(93, 93)
        )# 
img_array = tf.keras.utils.img_to_array(img) # 
img_array = tf.expand_dims(img_array, 0) # Create a batch


feature_maps=visualize_model.predict(img_array)
print(len(feature_maps))

# Show names of layers available in model
layer_names = [layer.name for layer in model.layers]
print(layer_names)

# import required libraries
import numpy as np
import matplotlib.pyplot as plt

y = 0
# Plotting the graph
for layer_names, feature_maps in zip(layer_names,feature_maps):
  
  if y<60:
    y += 1
    print(feature_maps.shape , ',' , layer_names)
    """ if len(feature_maps.shape) == 4 :
        channels = feature_maps.shape[-1]
        size = feature_maps.shape[1]
        display_grid = np.zeros((size, size * channels))
        for i in range(channels):
            x = feature_maps[0, :, :, i]
            x -= x.mean()
            x /= x.std()
            x *= 64
            x += 128
            x = np.clip(x, 0, 255).astype('uint8')
            # We'll tile each filter into this big horizontal grid
            display_grid[:, i * size : (i + 1) * size] = x

        scale = 20. / channels
        plt.figure(figsize=(scale * channels, scale))
        plt.title(layer_names)
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis') """
    
plt.show()

