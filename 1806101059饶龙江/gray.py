import cv2 as cv
import numpy as np
#import  matplotlib.pyplot as plt
#一般灰度化方法
def gray_pixels(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            a = image[i][j]
            g = 0.59*a[0]+0.11*a[1]+a[2]*0.30
            image[i][j]=g
    cv.imshow("gary image",image)
    print(image.shape)

#改进的灰度化方法：由于处理火灾图像时，需要突出火焰区域，所以可以改变权值的取值范围，使得火焰区域明显。
def chgray_pixels(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            a = image[i][j]
            g = 0*a[0]+0*a[1]+1*a[2]#示例
            image[i][j]=g
    cv.imshow("gary image",image)


src = cv.imread("D:/pecture/T0t0.jpg")#gbr
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#src_mind =  cv.medianBlur(src,5)
#cv.imshow("input image",src_mind)
cv.imshow("input image",src)
chgray_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()

#滤波的几个基本方法
#均值滤波：
#中值滤波
#高斯滤波
#双边滤波

