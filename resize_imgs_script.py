"""This script takes the path of the directory where the images are contained
and resizes all the images to a specific size (x*y) and stores all the images
to a directory specified.

Usage
-----
Enter the Source Directory path: ''
Enter the Destination Directory path: ''
Enter size: 'x*y'
"""
print('The script starts.')

import time

tik = time.time()
print(tik)

import os
import cv2

source_path = input('Enter the Source Directory path: ')
destination_path = input('Enter the Destination Directory path: ')

size = input('Enter the Size in Width*Height format: ')
size_splitted = size.split('*')
size_width = int(size_splitted[0])
size_height = int(size_splitted[1])

# Listing all the files from the Source Directory
files = os.listdir(source_path)
# Now this line of codes also catches some files those are not necessary and
# even not visible by the File Manager GUI. So let's make another list that
# will exclude thsoe files.
files = [file for file in files if file[-1] != '~']

no_of_files = len(files)
print('There are a total of {} files in the Source Directory.'.format(no_of_files))

print('Process on progress..')

for file in files:
    file_path = source_path + file
    inst_img = cv2.imread(file_path)
    inst_img_resized = cv2.resize(inst_img, (size_width, size_height))

    file_saving_path = destination_path + file
    cv2.imwrite(file_saving_path, inst_img_resized)

tok = time.time()
print(tok)

time_taken = (tok - tik) * (10 ** (-1))

print('Script ends. Took {} seconds.'.format(time_taken))
