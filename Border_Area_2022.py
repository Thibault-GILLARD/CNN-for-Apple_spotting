import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import numpy as np#csv
import shutil


'''
My work is a continuation of a thesis done in 2011
During this thesis more than 20,000 photos of apples were taken and the presence of defects, stems or calyxes was recorded.
However, this description is only done in an area of interest: a circle centered on the apple with a diameter twice as 
small as the apple. Only we are using CNNs, so we are using square filters, so we are trying to isolate a square with the same 
centre as the circle and of length D (diameter of the circle).

A first function find_boarder(apple_image) takes in a picture of an apple to find and return the north-south-east and west edges of it.

The method display(image) also takes in an apple picture and displays the apple with the traces of the edges, the contour, the circle with 
D/2 and the corresponding square. The purpose of this function is to visualise the areas of interest and check the accuracy of the methods used.

The crop(image) function takes an input image and returns its crop version, whose crop points are defined by the find_boarder() function.

The crop_a_file(source_def, destination_def) method uses the crop() function to crop all the images in one folder to save them in another

'''

def find_boarder(apple_image):
    #NS--- Luminosite
    #Find North boarder
    n=0
    s=0
    e=0
    w=0
    for i in range(15,190):
        r,v,b=apple_image.getpixel((320,i))
        #print(r,v,b)
        lumi=r+v+b
        if lumi > 130:
            n=i
            break 
    #print(n)

    #Find South boarder
    for i in range(455, 300, -1):
        r,v,b=apple_image.getpixel((320,i))
        lumi=r+v+b
        if lumi > 130:
            s=i
            break 
    #print(s)

    #EW--- presence de bleu
    #Find East boarder
    for i in range(20, 253):
        r,v,b=apple_image.getpixel((i,240))
        lumi=r+v+b
        #if lumi > 210:
        if lumi > 140:
            e=i
            break 
    #print(e)
    #Find West boarder
    for i in range(620, 380, -1):
        r,v,b=apple_image.getpixel((i,240))
        lumi=r+v+b
        #if lumi > 210:
        if lumi > 140:
            w=i
            break
    #print(w)

    return n, s, e, w

def affichage(image):
    im = Image.open(image)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(im)

    #Big Rect -----
    n, s, e, w = find_boarder(im)
    print(n, s, e, w,)
    # Create a Rectangle patch
    rect = patches.Rectangle((w, n), e-w, s-n, linewidth=1, edgecolor='r', facecolor='none')
    # Add the patch to the Axes
    ax.add_patch(rect)

    #Area
    Apple_Diameter=((s-n)+(w-e))/2
    #circ = patches.Circle(((w-e)/2,(s-n)/2),Apple_Diameter/2, linewidth=1, edgecolor='b', facecolor='none')
    circ = patches.Circle((e+(w-e)/2,n+(s-n)/2),Apple_Diameter/2, linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(circ)

    #circle 50% Area
    Apple_Diameter=((s-n)+(w-e))/2
    #circ = patches.Circle(((w-e)/2,(s-n)/2),Apple_Diameter/2, linewidth=1, edgecolor='b', facecolor='none')
    small_circ = patches.Circle((e+(w-e)/2,n+(s-n)/2),Apple_Diameter/4, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(small_circ)

    #rectangle 50% Area
    small_rect = patches.Rectangle(((-(Apple_Diameter/4)+e+(w-e)/2, n+(s-n)/4)), Apple_Diameter/2, Apple_Diameter/2, linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(small_rect)
    plt.show()

def crop(image):

    im = Image.open(image)

    
    n, s, e, w = find_boarder(im)
    Apple_Diameter=((s-n)+(w-e))/2
    centre_x=e+(w-e)/2
    centre_y=n+(s-n)/2
    
    # Size of the image in pixels (size of original image)
    width, height = im.size
    
    # Setting the points for cropped image
    left = centre_x-Apple_Diameter/3.9
    top = centre_y-Apple_Diameter/3.9
    right = centre_x+Apple_Diameter/3.9
    bottom = centre_y+Apple_Diameter/3.9
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    #im1.show()
    return im1

def crop_a_file(source_def, destination_def):

    source = source_def
    destination =destination_def

    files = os.listdir(source)#list mame of the file

    #for all files in the source folder
    for file in files:
        print(file)
        image_crop=crop(source + '\\'  + file)#we crop the image with the crop() function coded above
        image_crop.save(destination+'\\' + file, 'BMP')#save the crop image under the same name in BMP format

START = r'J:\Braeburn clean\Braeburn\Equatorial\Cam A'
STOP = r'J:\Braeburn clean\Braeburn_crop'


#crop_a_file(START, STOP)

affichage(r'J:\Braeburn clean\Braeburn\Equatorial\Cam A\8_100 33179706.bmp')