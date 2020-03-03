
import cv2 as cv

def yasuo(img):
    w,h=img.shape

    if w>=h and w>480:
        a=w/480
        b=h*a
        img=cv.resize(img,(480,b))

    elif h>=w and h>480:
        a=h/480
        b=w*a
        img=cv.resize(img,(b,480))
    else:
        pass
    return img







