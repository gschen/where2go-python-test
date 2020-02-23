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
        list=[]
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

                img = cv.bilateralFilter(image, 9, 75, 75)# 使用双边滤波去掉点状噪声
                image = cv.bilateralFilter(image, 9, 75, 75)  # 使用双边滤波去掉点状噪声
        #求图像火焰区域的Ud值

                #图像二值化
                max_g = 0
                best_T = 0
                r, c = img.shape
                N = r * c
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
                        best_T = T
                for i in range(r):
                    for j in range(c):
                        if img[i][j] < best_T:
                            img[i][j] = 0
                        else:
                            img[i][j] = 255

                M=img[255].sum()#统计疑似火焰图像的像素点个数
                r=0
                for i in range(1,h):
                    for j in range(1,w):
                        if img[i][j]==255:
                            r0=0
                            if img[i+1][j]==255:
                                r0=r0+image[i+1][j]
                            if img[i][j+1]==255:
                                r0=r0+image[i][j+1]
                            if img[i-1][j]==255:
                                r0=r0+image[i-1][j]
                            if img[i][j-1]==255:
                                r0=r0+image[i][j-1]
                            r=r+abs(image[i][j]-r0)
                            Ud=r/M
                            list.append(Ud)




                # src_bilater = cv.bilateralFilter(image, 9, 75, 75)
                # kernel = np.ones((1 * 2), np.uint8)  # 设置1*2的结构元素
                # dilata1 = cv.dilate(src_bilater, kernel, iterations=1)  # 用结构元素腐蚀图像
                # kerne2 = np.ones((3 * 1), np.uint8)  # 设置新的结构元素
                # image = cv.erode(dilata1, kerne2, iterations=1)  # 用结构元素进行数字信息的膨胀
                # w1 = int(w / 4)
                # w2 = int(w / 2)
                # w3 = int(3 * w / 4)
                # w0 = 0
                # img1 = image[h, w0:w1]
                # img2 = image[h, w1:w2]
                # img3 = image[h, w2:w3]
                # img4 = image[h, w3:w]

                # cv.imwrite('{}/img1/{}'.format(filename, i), image)
                #cv.imwrite('{}/img2/{}'.format(filename, i), img2)
                #cv.imwrite('{}/img3/{}'.format(filename, i), img3)
                #cv.imwrite('{}/img4/{}'.format(filename, i), img4)
            if k == number:
                break
    return  list
cut_p(path,filename,200)

cv.waitKey(0)
cv.destroyAllWindows()
















