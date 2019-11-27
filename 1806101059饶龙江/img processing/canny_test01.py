import cv2 as cv
import numpy as np
src = cv.imread("imgs/fire/t0000.jpg")

list1 = []
for i in range(len(src)-2):
    for j in range(len(src[i])-2):
        a=src[i][j]
        g=a[0]*0.6+a[1]*0.1+a[2]*0.3
        src[i][j]=g
        list1.append(src[i][j][0])
        list1.append(src[i+1][j][0])
        list1.append(src[i][j+1][0])
        list1.append(src[i-1][j][0])
        list1.append(src[i][j-1][0])
        list1.append(src[i+1][j+1][0])
        list1.append(src[i-1][j-1][0])
        list1.append(src[i+1][j-1][0])
        list1.append(src[i-1][j+1][0])
        if src[i][j][0] != np.max(list1):
            src[i][j]=0
        else:
            pass


cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
'''src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
img = cv.Canny(src,100,200)
cv.imshow("input image",img)
'''
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()