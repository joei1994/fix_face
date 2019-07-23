from flask import Flask, request, Response
import jsonpickle

import numpy as np
import cv2
import imutils
import dlib
from utils import rotate

app = Flask(__name__)

@app.route('/fix_face', methods=['POST'])
def fix_face():
    r = request
    image = np.fromstring(r.data, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    detector = dlib.get_frontal_face_detector()

    '''
    dlib provides face detector which detects only faces that are in the right orientation.
    my approach is simple, try to rotate original picture with every angels and if dlib's face detector can detect some faces 
    it means we have to fix original picture with that angel
    '''
    angels = [0, 90, 180, 270]
    for angel in angels:
        rotated_gray_image = rotate(gray_img, angel)
        rects = detector(rotated_gray_image, 1)
        if len(rects) > 0:
            break
        
    response = {
        'fixing_angel' : str(angel)
    }
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled,
     status=200, 
     mimetype="application/json")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)