"""This Script takes all the files from a specific folder and attact the Class 
Label to the front of each file name.

Usage
-----
Enter the Source Directory path:
Enter the Destination Directory path: 
Enter the Class Label: 
"""
print('The script starts.')

import time

tik = time.time()
print(tik)

import os

source_path = input('Enter the Source Directory path: ')
destination_path = input('Enter the Destination Directory path: ')
class_label = input('Enter the Class Label: ')

# Listing all the files from the Sowurce Directory
files = os.listdir(source_path)
# Now this line of codes also catches some files those are not necessary and
# even not visible by the File Manager GUI. So let's make another list that
# will exclude thsoe files.
files = [file for file in files if file[-1] != '~']

no_of_files = len(files)
print('There are a total of {} files in the Source Directory.'.format(no_of_files))

print('Process on progress..')

for file in files:
    inst_file_path = source_path + file
    inst_file = open(inst_file_path, 'rb')
    # print(inst_file.read())

    new_file_name = class_label + '_' + file
    new_file_path = destination_path + new_file_name

    create_new_file = open(new_file_path, 'wb')
    create_new_file.write(inst_file.read())

    inst_file.close()
    create_new_file.close()

tok = time.time()
print(tok)

time_taken = (tok - tik) * (10 ** (-1))

print('Script ends. Took {} seconds.'.format(time_taken))
