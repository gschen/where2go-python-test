import cv2 as cv
import numpy as np
import os


path ='D:\PYTHON\pycode\dev\\1806101059raolongjiang\img processing\imgs\sctu_codes'
filename = 'C:\sc'

def cut_p(path,filename,number):
    judge = os.path.exists(filename + '\\img1')
    if judge == False:
        os.chdir(filename)  # 相当于liunx里的cd
        now = os.getcwd()  # 获取当前地址，也就是上一行代码所进入的地址filename
        os.makedirs(now + '\\img1')
        imagelist = os.listdir(path)  # 读取path目录下所有文件的名字
        k = 0
        for i in imagelist:
            k += 1
            if (i.endswith('.jpg' or '.png')):
                # 如果文件以jpg结尾
                image = cv.imread(path + '/' + i)
                hw = image.shape
                h = hw[0]
                w = hw[1]
                for y in range(h):
                    for x in range(w):
                        # 将图像灰度化
                        a = image[y][x]
                        g = 0.59 * a[0] + 0.11 * a[1] + 0.30 * a[2]
                        image[y][x] = g  # 灰度化
                src_bilater = cv.bilateralFilter(image, 9, 75, 75)
                kernel = np.ones((1 * 2), np.uint8)  # 设置1*2的结构元素
                dilata1 = cv.dilate(src_bilater, kernel, iterations=1)  # 用结构元素腐蚀图像
                kerne2 = np.ones((3 * 1), np.uint8)  # 设置新的结构元素
                image = cv.erode(dilata1, kerne2, iterations=1)  # 用结构元素进行数字信息的膨胀
                w1 = int(w / 4)
                w2 = int(w / 2)
                w3 = int(3 * w / 4)
                w0 = 0
                img1 = image[h, w0:w1]
                img2 = image[h, w1:w2]
                img3 = image[h, w2:w3]
                img4 = image[h, w3:w]
                cv.imwrite('{}/img1/{}'.format(filename, i), img1)
                #cv.imwrite('{}/img2/{}'.format(filename, i), img2)
                #cv.imwrite('{}/img3/{}'.format(filename, i), img3)
                #cv.imwrite('{}/img4/{}'.format(filename, i), img4)
            if k == number:
                break
cut_p(path,filename,1000)

cv.waitKey(0)
cv.destroyAllWindows()
















