'''import cv2 as cv
import numpy as np
def fenge(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            a = img[i][j]
            for t in range(256):
                if a > t:
                    a = 0
                else:
                    a = 255'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("......")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(131), plt.imshow(image, "gray")
plt.title("source image"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.hist(image.ravel(), 256)
plt.title("Histogram"), plt.xticks([]), plt.yticks([])
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU
plt.subplot(133), plt.imshow(th1, "gray")
plt.title("OTSU,threshold is " + str(ret1)), plt.xticks([]), plt.yticks([])
plt.show()





src = cv.imread("imgs/fire/7.PNG")#gbr
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)