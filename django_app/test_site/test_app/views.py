from django.shortcuts import render

# Self added codes.
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.


def index(request):
    # Getting POST data from the request object.
    # first_number = request.POST['first_number']
    # second_number = request.POST['second_number']

    # Getting FILE data from the request object.
    # file = request.FILES['test_file']

    # Saving file to Django server.
    # ext = str(file).split('.')[1]
    # f = open('test_app/uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'wb')
    # f.write(file.read())
    # f.close()

    # Response Strings.
    return_str = 'A Response from the Djanog app.'
    # return_str = '{}, {}.'.format(first_number, second_number)
    # return_str = str(int(first_number) + int(second_number))
    # return_str = 'The file named as {} has been uploaded to the ' \
    #     'server at \'test_app/uploaded_files\'.'.format(str(file))

    # Creating a 'FileRespose' object.
    # f = open('test_app/uploaded_files/uploaded_file_{}.{}'.format(str(1), ext), 'rb')
    # return_file_response = FileResponse(f)

    # Returning the Respose.
    return HttpResponse(return_str)
    # return HttpResponse(return_file_response)


def character_classifier(request):
    import os
    script_path = os.path.abspath(__file__)
    base_path_arr = script_path.split('/')
    base_path_arr = base_path_arr[0: len(base_path_arr) - 1]
    base_path = '/'.join(base_path_arr) + '/'

    # Getting FILE data from the request object.
    file = request.FILES['test_file']

    # Saving file to Django server.
    ext = str(file).split('.')[1]
    # file_path = 'test_app/uploaded_files/uploaded_file_{}.{}'.format(
    #     str(1), ext)
    file_path = base_path + 'uploaded_files/uploaded_file_{}.{}'.format(
        str(1), ext)

    f = open(file_path, 'wb')
    f.write(file.read())
    f.close()

    # Importing the Model.
    import tensorflow as tf
    # model = tf.keras.models.load_model('test_app/models/model_1/')
    model = tf.keras.models.load_model(base_path + 'models/model_1/')

    # Grabing the file.
    import cv2
    img = cv2.imread(file_path)
    # Resizing the Image.
    resized_img = cv2.resize(img, (32, 32))
    # Flattening the Imgae array.
    resized_img = resized_img.reshape(-1, 32 * 32 * 3)

    # Making prediction using our Model.
    prediction = model.predict(resized_img)

    import numpy as np
    class_index = np.argmax(prediction)

    classes = ['0-Alpha', '1-Beta', '2-Gamma']
    class_ = classes[class_index]

    return_str = '\'' + class_ + '\'' + ' ' + 'This Project is made by \'Sai Nilayam Sahu\'.' \
        + ' Find awesome AI Services at \'www.aiwebsites.in\'.'

    return HttpResponse(return_str)
    # return HttpResponse('Completed')
