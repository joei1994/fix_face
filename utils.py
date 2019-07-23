import cv2

def rotate(img, angel):
    shapes = img.shape
    if len(shapes) == 3:
        h, w, _ = shapes
    else: 
        h, w = shapes

    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angel, scale=1)
    rotated_img = cv2.warpAffine(img, M, (h, w))
    return rotated_img