import os
import requests

url = "http://118.42.59.85:5000/api1"
image_file_descriptor = open('face/LEE.jpg', 'rb')
# Requests makes it simple to upload Multipart-encoded files
files = {'media' : image_file_descriptor}
requests.post(url, files=files)
image_file_descriptor.close()