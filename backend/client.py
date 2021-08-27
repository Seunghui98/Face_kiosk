import requests
import base64

with open('LEE.jpeg', 'rb') as f:
    im_b64 = base64.b64encode(f.read())

payload = {'type': 'jpeg', 'image': im_b64}

url = "http://localhost:8080/upload"

r = requests.post(url, data=payload)

# convert server response into JSON format.
print(r.json())