"""This script takes the path of the directory where the images are contained
and augment the images as per the parameters specified by user, then saves the
augmented images to the destination directory.

Usage
-----
Enter the Source Directory path: ''
Enter the Destination Directory path: ''

Available types: 1. Lighting, 2.Stretching, 3.Rotating
Enter Augmentation types in space separated format: ''

Enter Values for Lighting in space separated: ''
Enter Values for Streting in space separeated: ''
Enter Values for Rotating in space separated: ''

'Description of the operations'

Enter y for yes, else type anything to abort: ''
"""
print('The script starts.')

import time

tik = time.time()
print(tik)
# -----------------------------------------------------------------------------

import os
import cv2

source_path = input('Enter the Source Directory path: ')
destination_path = input('Enter the Destination Directory path: ')

print('\n Available types: 1. Lighting, 2.Stretching, 3.Rotating')
augmetation_types = input(
    'Enter Augmentation types in space separated format: ')
# Augmentaion types array defined.
augmentaion_types = augmentaion_types.split(' ')

for type_ in augmentaion_types:
    if type_ == '1':
        print('Available Values are: -30, -20, -10, 10, 20, 30 in Units')
        lighting_values = input('Enter Lighting Values in space separated: ')
        # Lighting Values defined.
        lighting_values = lighting_values.split(' ')
    if type_ == '2':

        stretching_values = input(
            'Enter Stretching Values in space separated: ')
        # Stretching Values defined.
        stretching_values = stretching_values.split(' ')
    if type_ == '3':
        print('Available Values are: -30, -20, -10, 10, 20, 30 in Degrees')
        rotating_values = input('Enter Rotating Values in space separated: ')
        # Rotating Values defined.
        rotating_values = rotating_values.split(' ')


def lighting_change(img, lighting_value):
    new_img = img + lighting_value
    return new_img

def stretching_change(img, stretching_value):



    # -----------------------------------------------------------------------------
tok = time.time()
print(tok)

time_taken = (tok - tik) * (10 ** (-1))

print('Script ends. Took {} seconds.'.format(time_taken))
