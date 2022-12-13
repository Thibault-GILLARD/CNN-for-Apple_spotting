

import cv2
import tensorflow as tf
import numpy as np
import time
time_duration = 2

#images
apple0 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T3 Granny Smith_trie\Team\test\0 nothing\527000.BMP'
apple1 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T3 Granny Smith_trie\Team\test\1stem\8530110.BMP'
apple2 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T3 Granny Smith_trie\Team\test\2calyx\313200.BMP'
apple3 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T3 Granny Smith_trie\Team\test\3defect\1606300.BMP'
apple_other =r'C:\Users\tgillard\Desktop\internship\DATA_SET\T2 Eve_trie\Team\test\0 nothing\2219000.BMP'

liste = [apple0, apple1, apple2,apple3,apple_other]

apple_lab0 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T5 Apple_Lab\small\0 nothing\1.bmp'
apple_lab1 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T5 Apple_Lab\small\1stem\1.bmp'
apple_lab2 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T5 Apple_Lab\small\2calyx\1.bmp'
apple_lab3 = r'C:\Users\tgillard\Desktop\internship\DATA_SET\T5 Apple_Lab\small\3defect\1.bmp'

liste_lab = [apple_lab0, apple_lab1, apple_lab2,apple_lab3]

model = tf.keras.models.load_model(r"C:\Users\tgillard\Desktop\internship\tanining\last_night-97.71.h5")
model2 = tf.keras.models.load_model(r"C:\Users\tgillard\Desktop\internship\tanining\fruitTotalT1_1-95.14.h5")
class_names = ['0 nothing','1stem','2calyx','3defect']


""" img = tf.keras.utils.load_img(
    liste[0], target_size=(93, 93)#\\\\\
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
print(score)
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)  """

def pred_list(list):
    for i in range (len(list)):
        
        img = tf.keras.utils.load_img(
            list[i], target_size=(93, 93)#\\\\\
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        print(score)

        print(
            " {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )

pred_list(liste_lab)