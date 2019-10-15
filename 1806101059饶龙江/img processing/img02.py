import numpy as np
import cv2 as cv
import os
src=cv.imread("D:/pecture/T0t0.jpg")
cv.namedWindow("src",cv.WINDOW_AUTOSIZE)
cv.imshow('src',src)
src=np.array(src)
#手动添加椒盐噪声
def zaos(src,pro):
    '''print(type(src))
    print(src.shape)
    print(src.size)
    print(src.dtype)
    pixel_data = np.array(src)
    print(pixel_data)'''

    for i in range(len(src)-3):
        for j in range(len(src[i])-3):
            if np.random.rand()<pro:
                src[i][j] = [0,0,0]
                src[i+1][j] = [0, 0, 0]
                src[i][j+1] = [0, 0, 0]
                src[i+1][j+1] = [0, 0, 0]
                src[i+2][j] = [0, 0, 0]
                src[i][j+2] = [0, 0, 0]
                src[i+2][j+2] = [0, 0, 0]
                src[i+2][j+1] = [0, 0, 0]
                src[i+1][j+2] = [0, 0, 0]
    return src

img=zaos(src,0.01)
#os.chdir('D:\\pecture')
cv.namedWindow("img",cv.WINDOW_AUTOSIZE)
cv.imshow('img',img)
cv.imwrite("D:\\pecture\\椒盐噪声图.png",img)
cv.waitKey(0)
cv.destroyAllWindows()