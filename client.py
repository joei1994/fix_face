from __future__ import print_function
import requests
import json
import cv2
import os
import numpy as np
from utils import rotate
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())

#image_path = os.path.join('./images', 'ronaldo.jpg')

addr = 'http://localhost:80'
test_url = addr + '/fix_face'

# prepare headers 
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread(args["image"])
# encode image 
_, img_encoded = cv2.imencode('.jpg', img)

# send request with image
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

# handle response
response = json.loads(response.text)
fixing_angel = int(response['fixing_angel'])
print(f"fixing angel : {fixing_angel}")
fixed_img = rotate(img, fixing_angel)
cv2.imwrite('result.jpg', fixed_img)
