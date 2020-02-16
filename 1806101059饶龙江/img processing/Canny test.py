import cv2 as cv
import numpy as np
import math


src = cv.imread("imgs/fire/u=1463018956,861119745&fm=26&gp=0.jpg")
img = cv.cvtColor(src,cv.COLOR_BGR2GRAY)


#创建高斯矩阵
sigma1 = sigma2 = 1
sum = 0
gaussian = np.zeros([5, 5])
for i in range(5):
    for j in range(5):
        gaussian[i, j] = math.exp(-1 / 2 * (np.square(i - 3) / np.square(sigma1) + (np.square(j - 3) / np.square(sigma2)))) / (2 * math.pi * sigma1 * sigma2)
        sum = sum + gaussian[i, j]
gaussian = gaussian / sum
print(gaussian)
#高斯滤波
w =img.shape[0]
h =img.shape[1]
new_gray = np.zeros([w-5,h-5])#创建一个新的数组，用于存储高斯滤波之后的图像信息
for i in range(w-5):
    for j in range(h-5):
        new_gray[i,j] = np.sum(img[i:i+5,j:j+5]*gaussian)#使用卷积的方法进行高斯滤波


#计算梯度幅度(1), 数字图像处理中，用一阶有限差分近似求取灰度值的梯度值(变化率)。
# 即：使差商(Δf-Δx)近似取代微商(∂f/∂x)。求灰度的变化率，分别取x和y方向上相邻像素做差，代替求取x和y 方向一阶偏导
w1=new_gray.shape[0]
h1=new_gray.shape[1]
dx = np.zeros([w1-1, h1-1])
dy = np.zeros([w1-1, h1-1])
d = np.zeros([w1-1, h1-1])
for i in range(w1-1):
    for j in range(h1-1):
        dx[i,j] = new_gray[i, j+1] - new_gray[i, j]
        dy[i,j] = new_gray[i+1, j] - new_gray[i, j]
        d[i, j] = np.sqrt(np.square(dx[i,j]) + np.square(dy[i,j]))
cv.imshow("gray",img)
cv.imshow("img",d)
cv.imshow("new_gray",new_gray)
#使用soble算子






cv.waitKey(0)
cv.destroyAllWindows()






