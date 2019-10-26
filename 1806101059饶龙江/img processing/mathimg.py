import cv2 as cv
import numpy as np

src = cv.imread("imgs/fire/code.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#cv.imshow("input",src)
print(src.shape)
#将图像放大5倍。
w = src.shape[0]
h = src.shape[1]
src1 = cv.resize(src,(5*h,5*w),interpolation=cv.INTER_CUBIC)
cv.imshow("fangda",src1)
#灰度化图像：
def gray_pixels(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            a = image[i][j]
            g = 0.59*a[0]+0.11*a[1]+a[2]*0.30#工业电视标准
            image[i][j]=g
    #cv.imshow("gary image",image)

#膨胀
'''kernel = np.ones((2*2),np.uint8)
erode = cv.erode(img,kernel,iterations=1)
#腐蚀
kernel = np.ones((2*2),np.uint8)
dilata1 = cv.dilate(img,kernel,iterations=1)
dilata2 = cv.dilate(dilata1,kernel,iterations=1)
#cv.imshow("open img",erode)
#cv.imshow("dilata img",dilata2)


# 均值滤波：
src_mean = cv.blur(img, (5, 5))
# 中值滤波：
src_mind = cv.medianBlur(img, 7)
# 高斯滤波：
src_Guassian = cv.GaussianBlur(img, (3,3 ), 0)
# 双边滤波：
src_bilater = cv.bilateralFilter(img, 9, 75, 75)

#cv.imshow("src_Guassian",src_Guassian)
#cv.imshow("mind",src_mind)
#cv.imshow("menan",src_mean)
cv.imshow("bilater",src_bilater)#根据不同滤波方法的对比，发现双边滤波对于验证码图片的滤波效果最好，
故选用双边滤波法。
'''


cv.waitKey(0)
cv.destroyAllWindows()