import  cv2 as cv
import numpy as np
import math
#基于个数的中值滤波
src = cv.imread("imgs/fire/7.PNG")
def number_mind(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            a = img[i][j]
            g = 0.59*a[0] +0.11* a[1] + 0.30*a[2]
            img[i][j] = g
    cv.imshow("image",img)
    s = 0
    list = []
    t = 25#手动设置阈值
    for k in range(len(img)-2):
        for l in range(len(img[k])-2):
            #记录3*3区域的像素点灰度值
            m0 = img[k][l]
            m1 = img[k+1][l]
            m2 = img[k][l+1]
            m3 = img[k-1][l]
            m4 = img[k][l-1]
            m5 = img[k+1][l+1]
            m6 = img[k-1][l-1]
            m7 = img[k+1][l-1]
            m8 = img[k-1][l+1]
           #记录灰度值差值，并将它们加入列表
            o1 = abs(int(m1[1]) - int(m0[1]))#在此处需要注意将数值强制转化成整型，否则会出现数据溢出的错误。
            list.append(o1)
            o2 = abs(int(m2[1]) - int(m0[1]))
            list.append(o2)
            o3 = abs(int(m3[1]) - int(m0[1]))
            list.append(o3)
            o4 = abs(int(m4[1]) - int(m0[1]))
            list.append(o4)
            o5 = abs(int(m5[1]) - int(m0[1]))
            list.append(o5)
            o6 = abs(int(m6[1]) - int(m0[1]))
            list.append(o6)
            o7 = abs(int(m7[1]) - int(m0[1]))
            list.append(o7)
            o8 = abs(int(m8[1]) - int(m0[1]))
            list.append(o8)
            list1 = sorted(list)#对列表进行排序
            #判断灰度值差的绝对值是否大于阈值，并统计他们的个数
            for li in list1:
                if li >= t :
                    s =s +1
            if s > 6 :
                m0 = list1[4]+m0
                img[k][l] = m0

    cv.imshow("src",img)
number_mind(src)
cv.waitKey(0)
cv.destroyAllWindows()




















