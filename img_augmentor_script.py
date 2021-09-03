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

Testings
--------
/home/sai-nilayam/Desktop/dev/project_2/data/train/training_data/

/home/sai-nilayam/Desktop/dev/project_2/data/train/training_data_augmented/

-30 -20 -10 10 20 30
"""
print('The script starts.')

import time

tik = time.time()
print(tik)
# -----------------------------------------------------------------------------

import os
import cv2
from PIL import Image
import numpy as np

source_path = input('Enter the Source Directory path: ')
destination_path = input('Enter the Destination Directory path: ')

print('\nAvailable types: 1.Lighting, 2.Stretching, 3.Rotating')
augmentation_types = input(
    'Enter Augmentation types in space separated format: ')
# Augmentaion types array defined.
augmentation_types = augmentation_types.split(' ')

for type_ in augmentation_types:
    if type_ == '1':
        print('Available Values are: -30, -20, -10, 10, 20, 30 in Units of 0-255')
        lighting_values = input('Enter Lighting Values in space separated: ')
        # Lighting Values defined.
        lighting_values = lighting_values.split(' ')
    if type_ == '2':
        print('Available Values are: -30, -20, -10, 10, 20, 30 in Percent.')
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
    initial_width = img.shape[1]
    initial_height = img.shape[0]
    # Getting the Inital Width and Height of the Image.
    new_width = round(
        initial_width + (initial_width * (stretching_value / 100)))
    new_height = round(
        initial_height + (initial_height * (stretching_value / 100)))
    # Calculating the new Width and Height.
    new_img_1 = cv2.resize(img, (new_width, initial_height))
    new_img_2 = cv2.resize(img, (initial_width, new_height))

    return (new_img_1, new_img_2)


def rotating_change(img, rotating_value):
    # Converting the img array to PIL img.
    img = Image.fromarray(img)
    new_img = img.rotate(rotating_value)
    # Converting back the PIL img to Open CV type Numpy array.
    new_img = np.array(new_img)

    return new_img

# Now we have the variable availables are
# source_directory_path
# destination_directory_path
# augmentation_types
# lighting_values
# stretching_values
# rotating_values


# Now the first step is to list all the img files from the Source Directory.
files = os.listdir(source_path)
# Now this line of codes also catches some files those are not necessary and
# even not visible by the File Manager GUI. So let's make another list that
# will exclude thsoe files.
files = [file for file in files if file[-1] != '~']

no_of_files = len(files)
print('There are a total of {} files in the Source Directory.'.format(no_of_files))

print('Process on progress..')

# Now open each file using it's path and apply all three types of augmentations
# and save them all according to the augmentaion values in the respective
# arrays.

for file in files:
    file_path = source_path + file
    inst_img = cv2.imread(file_path)

    if '1' in augmentation_types:
        # Applying Lightings.
        for value in lighting_values:
            value = int(value)
            inst_img_lighten = lighting_change(inst_img, value)

            # Image saving path
            file_saving_path = destination_path + \
                file.split('.')[0] + '_lighten_' + str(value) + '.jpg'
            cv2.imwrite(file_saving_path, inst_img_lighten)

    if '2' in augmentation_types:
        # Applying Stretchings.
        for value in stretching_values:
            value = int(value)
            inst_img_stretched_1, inst_img_stretched_2 = stretching_change(
                inst_img, value)

            # Image saving path
            file_saving_path = destination_path + \
                file.split('.')[0] + '_stretched_' + str(value) + '_1' + '.jpg'
            cv2.imwrite(file_saving_path, inst_img_stretched_1)
            file_saving_path = destination_path + \
                file.split('.')[0] + '_stretched_' + str(value) + '_2' + '.jpg'
            cv2.imwrite(file_saving_path, inst_img_stretched_2)

    if '3' in augmentation_types:
        # Applying Rotations.
        for value in rotating_values:
            value = int(value)
            inst_img_rotated = rotating_change(inst_img, value)

            # Image saving path
            file_saving_path = destination_path + \
                file.split('.')[0] + '_rotated_' + str(value) + '.jpg'
            cv2.imwrite(file_saving_path, inst_img_rotated)


# -----------------------------------------------------------------------------
tok = time.time()
print(tok)

time_taken = (tok - tik) * (10 ** (-1))

print('Script ends. Took {} seconds.'.format(time_taken))
