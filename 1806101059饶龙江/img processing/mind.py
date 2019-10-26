import  cv2 as cv
import numpy as np


#基于个数的中值滤波
src = cv.imread("imgs/fire/code.jpg")
def number_mind(src):
    for i in range(len(src)):
        for j in range(len(src[i])):
            a = src[i][j]
            g = a[0] + a[1] + a[2]
            src[i][j] = g
    s = 0
    list = []
    t = 125
    for k in range(len(src)-2):
        for l in range(len(src[k])-2):
            m0 = src[k][l]
            m1 = src[k+1][l]
            m2 = src[k][l+1]
            m3 = src[k-1][l]
            m4 = src[k][l-1]
            m5 = src[k+1][l+1]
            m6 = src[k-1][l-1]
            m7 = src[k+1][l-1]
            m8 = src[k-1][l+1]

            o1 = m1[0]-m0[0]
            list.append(o1)
            o2 = m2[0]-m0[0]
            list.append(o2)
            o3 = m3[0]-m0[0]
            list.append(o3)
            o4 = m4[0]-m0[0]
            list.append(o4)
            o5 = m5[0]-m0[0]
            list.append(o5)
            o6 = m6[0]-m0[0]
            list.append(o6)
            o7 = m7[0]-m0[0]
            list.append(o7)
            o8 = m8[0]-m0[0]
            list.append(o8)
        list1 = sorted(list)
        for li in list1:
            if li >= t :
                s =s +1
        if s > 6 :
            m0 = list1[4]
        cv.imshow("mind img",src)
number_mind(src)
cv.waitKey(0)
cv.destroyAllWindows()




















