import cv2 as cv
import numpy as np
from PIL import Image

def Laplace_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    L_sunnzi = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    #L_sunnzi = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    for i in range(r - 2):
        for j in range(c - 2):
            new_image[i + 1, j + 1] = abs(np.sum(img[i:i + 3, j:j + 3] * L_sunnzi))
    return np.uint8(new_image)

def chafenfa(img1,img2):
    r1,c1=img1.shape
    new_image = np.zeros((r1, c1))
    for i in range(r1):
        for j in range(c1):
            new_image[i][j]=abs(img1[i][j]-img2[i][j])
    return np.uint8(new_image)

def otsu_img(img):
    max_g = 0
    best_T= 0
    r,c=img.shape
    N=r*c
    for T in range(256):
        n0 = img[:T].sum()  # 阈值以下像素总数(前景)
        n1 = img[T:].sum()  # 阈值以上像素总数（背景）
        w0 = n0 / N  # 阈值以下像素数量占的比例（前景）
        w1 = n1 / N  # 阈值以上像素数量占的比例（背景）
        # 阈值以下平均灰度(前景)
        u0 = 0
        for i in range(T):
            u0 += i * img[i]

        # 阈值以上平均灰度(背景)
        u1 = 0
        for i in range(T, 256):
            u1 += i * img[i]

        # u = u0 * w0 + u1 * w1
        g = w0 * w1 * np.power((u0 - u1), 2)

        if g > max_g:
            max_g = g
            best_T=T
    for i in range(r):
        for j in range(c):
            if img[i][j]<best_T:
                img[i][j]=0
            else:
                img[i][j]=255


def dilation(img):#此时图像时二值化之后的图像，即只有0、1两个灰度值
    kernel=np.ones((2,2),np.uint8)#构建全是1的2*2数组
    r,c =img.shape
    for i in range(r-1):
        for j in range(c-1):
            if img[i+2][j+2].sum ==kernel.sum:#由于img图像中只有0和1，所以当它们区域和相等时，即完全重合
                img[i][j]=img[i][j]
            else:
                img[i][j]==0
    return img

def erosion(img):#此时图像时二值化之后的图像，即只有0、1两个灰度值
    kernel=np.ones((2,2),np.uint8)#构建全是1的2*2数组
    r,c =img.shape
    for i in range(r-1):
        for j in range(c-1):
            if sum(img[i+2][j+2]*kernel):#只要它们卷积和不为零，即可认为有交集。
                img[i][j]=img[i][j]
            else:
                img[i][j]==0
    return img

