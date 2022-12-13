import cv2
import tensorflow as tf
import time
import numpy as np

import os
import shutil

time_duration = 2

model = tf.keras.models.load_model(r"C:\Users\tgillard\Desktop\internship\0_Final_Code\1_Braeburn\Braeburn_21_11-97.19.h5")
class_names = ['0 nothing','1stem','2calyx','3defect']

#Source files are not  sorted
source = r'J:\Braeburn clean\Braeburn_crop'
#Destination (Sorted)
destination0 = r'J:\Braeburn clean\Baeburn_trie_model_aug\0 nothing'
destination1 = r'J:\Braeburn clean\Baeburn_trie_model_aug\1stem'
destination2 = r'J:\Braeburn clean\Baeburn_trie_model_aug\2calyx'
destination3 = r'J:\Braeburn clean\Baeburn_trie_model_aug\3defect'

files = os.listdir(source)#list mame of the file


v = 'J:\\Braeburn clean\\Braeburn_crop\\' + files[0]



def pred(pics):    
    pic = 'J:\\Braeburn clean\\Braeburn_crop\\' + pics
    img = tf.keras.utils.load_img(
        pic, target_size=(93, 93)#\\\\\
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
    return class_names[np.argmax(score)]


 
for file in files: 
    if pred(file)=='0 nothing':
        new_path = shutil.move(f"{source}/{file}", destination0)
        print(new_path)
    elif pred(file)=='1stem': 
        new_path = shutil.move(f"{source}/{file}", destination1)
        print(new_path)
    elif pred(file)=='2calyx': 
        new_path = shutil.move(f"{source}/{file}", destination2)
        print(new_path)
    elif pred(file)=='3defect':  
        new_path = shutil.move(f"{source}/{file}", destination3)
        print(new_path)