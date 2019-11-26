import cv2 as cv
import numpy as np
#import  matplotlib.pyplot as plt
#一般灰度化方法
def gray_pixels(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            a = image[i][j]
            g = 0*a[0]+0*a[1]+1*a[2]#示例
            image[i][j]=g

    #使用双边滤波去掉点状噪声
    image1 = cv.bilateralFilter(image, 9, 75, 75)

    cv.imshow("med image", image1)
    #利用腐蚀去掉线状噪声
    kernel = np.ones((1 * 2), np.uint8)
    dilata1 = cv.dilate(image1, kernel, iterations=1)
    # 使用膨胀对字母进行加粗
    kerne2 = np.ones((1 * 3), np.uint8)
    erode1 = cv.erode(dilata1, kerne2, iterations=1)
    kerne3 = np.ones((1 * 2), np.uint8)
    erode = cv.erode(erode1, kerne3, iterations=1)
    cv.imshow("dilata img", dilata1)
    cv.imshow("erode img", erode)
    '''
    mean = np.mean(dilata1[:,:,[0]])
    print(mean)
    for x in range(len(dilata1)):
        for y in range(len(dilata1[x])):
            b = dilata1[x][y][0]
            if b < mean:
                dilata1[x][y]=0
            else:
                dilata1[x][y]=255
    '''






    print(image.shape)

#改进的灰度化方法：由于处理火灾图像时，需要突出火焰区域，所以可以改变权值的取值范围，使得火焰区域明显。
def chgray_pixels(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            a = image[i][j]
            g = 0*a[0]+0*a[1]+1*a[2]#示例
            image[i][j]=g

    cv.imshow("gary image",image)


src = cv.imread("imgs/captchas/test_1.png")#gbr
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#膨胀
'''
kernel = np.ones((2*2),np.uint8)
erode = cv.erode(src,kernel,iterations=1)

#腐蚀
kernel = np.ones((2*2),np.uint8)
dilata1 = cv.dilate(src,kernel,iterations=1)
dilata2 = cv.dilate(dilata1,kernel,iterations=1)

#开运算；先腐蚀再膨胀
open = cv.morphologyEx(src,cv.MORPH_OPEN,kernel)
#闭运算；先膨胀后腐蚀
closing = cv.morphologyEx(src,cv.MORPH_CLOSE,kernel)
cv.namedWindow("open img",cv.WINDOW_AUTOSIZE)
cv.namedWindow("dilata img",cv.WINDOW_AUTOSIZE)
#cv.imshow("open img",erode)
cv.imshow("dilata img",dilata2)

# 滤波的几个基本方法
# 均值滤波：
src_mean = cv.blur(src, (5, 5))
# 中值滤波：
src_mind = cv.medianBlur(src, 7)
# 高斯滤波：
src_Guassian = cv.GaussianBlur(src, (3,3 ), 0)
# 双边滤波：
src_bilater = cv.bilateralFilter(src, 9, 75, 75)
cv.imshow("input image",src_mind)
'''
#chgray_pixels(src)
gray_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()
