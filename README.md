This is a Character Recogniser Application. The way it is intended to be used 
is, all you need to request to one of the page to our server with the required
parameters. Our Server will Respond you back with the appropriate answer.

Usage
-----
For Python users, Here is piece of code that explains the usage.

```python
import requests

# You must specify 'rb' parameter while opening the file.
# Specify the 'Path to the Image' here.
f = open('data/test/gamma/2_2.jpg', 'rb')

url = 'http://www.aiwebsites.in/test_app/character_classifier'

files = {
    'test_file': f,
}

# Pass the file dictionary as 'files' argument.
response = requests.post(url, files=files)

f.close()

# Getting the response code.
print(response)

# Getting the respose content.
print(response.content, end='\n')
print(respose.text)
```

Thank you for taking a look. 

Please ask any queries you want. I would be delight to answer all of the 
queries.