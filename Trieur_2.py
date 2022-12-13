#https://askcodez.com/comment-faire-pour-trier-les-noms-de-fichiers-dans-un-ordre-particulier-a-laide-de-python.html

'''
After renaming all the photo files, we can see which characteristics each apple has:
Key to tables:
The file name identifies the type of apple - Braeburn, Eve etc
The first three digits of the entry identify the apple
The next two digits identify the image
The next digit indicates if the is 0 - nothing, 1 - stem, 2 - calyx, 3 – defect
The next digit indicates object of interest near edge of search area
The last digit indicates sharpness of the image, 0 - sharp

Example:	00311110 in the Braeburn.txt file indicates
Image 003-11.bmp
A stem is present in the search area
An object of interest is close to the edge of the search area
The image is sharp

For each variety we will create 4 folders separating the apples according to the characteristics they have (default...)
'''

import os
import numpy as np#csv
import shutil

#Source files are not  sorted
source = r'C:\Users\tgillard\Desktop\internship\applepic\Trie\3 Granny Smith_trie\3 Granny Smith'
#Destination (Sorted)
destination0 = r'C:\Users\tgillard\Desktop\internship\applepic\Trie\T3 Granny Smith_trie\Basics\0 nothing'
destination1 = r'C:\Users\tgillard\Desktop\internship\applepic\Trie\T3 Granny Smith_trie\Basics\1stem'
destination2 = r'C:\Users\tgillard\Desktop\internship\applepic\Trie\T3 Granny Smith_trie\Basics\2calyx'
destination3 = r'C:\Users\tgillard\Desktop\internship\applepic\Trie\T3 Granny Smith_trie\Basics\3defect'

files = os.listdir(source)#list mame of the file
x=1
print(files[x][-7:])
print(files[x])

#the sorting
#If the file is not blurred ;
  #depending on the digit in the -7 slot, send the photo to a specific folder

'''
for file in files:
    if file[-5]=='0':  
        if file[-7]=='0':
            new_path = shutil.move(f"{source}/{file}", destination0)
            print(new_path)
        elif file[-7]=='1': 
            new_path = shutil.move(f"{source}/{file}", destination1)
            print(new_path)
        elif file[-7]=='2': 
            new_path = shutil.move(f"{source}/{file}", destination2)
            print(new_path)
        elif file[-7]=='3':  
            new_path = shutil.move(f"{source}/{file}", destination3)
            print(new_path)
'''
for file in files: 
    if file[-7]=='0':
        new_path = shutil.move(f"{source}/{file}", destination0)
        print(new_path)
    elif file[-7]=='1': 
        new_path = shutil.move(f"{source}/{file}", destination1)
        print(new_path)
    elif file[-7]=='2': 
        new_path = shutil.move(f"{source}/{file}", destination2)
        print(new_path)
    elif file[-7]=='3':  
        new_path = shutil.move(f"{source}/{file}", destination3)
        print(new_path)
