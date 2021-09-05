"""This script Requests to one of the URL of of our Django App and
shows the Respose.
"""

'''
"""For sending a Request with a string data to the server"""
import requests

# URL to the Django inbuilt server.
# url = 'http://127.0.0.1:8000/test_app/'
# URL to the Apache server.
url = 'http://127.0.0.1:80/test_app/'

data = {
    'first_number': 1,
    'second_number': 2
}

response = requests.post(url, data=data)

print(response)

print(response.content)
'''


"""For seding a Request with a file attached to it to server and getting 
a file as Response."""
import requests

img_path = input('Enter the path of the Image: ')

# You must specify 'rb' parameter while opening the file.
# f = open('data/test/gamma/2_2.jpg', 'rb')
f = open(img_path, 'rb')

# url = 'http://127.0.0.1:8000/test_app/'

url = 'http://127.0.0.1:80/test_app/character_classifier'
# url = 'http://127.0.0.1:8000/test_app/character_classifier'

files = {
    'test_file': f,
}

# Pass the file dictionary as 'files' argument.
response = requests.post(url, files=files)

f.close()

# Getting the response code.
print(response)

# Getting the respose content.
# print(response.content)
print(response.content)
