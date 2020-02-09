import cv2
import numpy as np
import math

""" 输入图像归一化 """


def stretch(img):
    max = float(img.max())
    min = float(img.min())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = (255 / (max - min)) * img[i, j] - (255 * min) / (max - min)

    return img


def dobinaryzation(img):
    max = float(img.max())
    min = float(img.min())

    x = max - ((max - min) / 2)
    ret, thresholdimg = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)

    return thresholdimg


def find_retangle(contour):
    y, x = [], []

    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])

    return [min(y), min(x), max(y), max(x)]


def locate_license(img, orgimg):
    img, contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 找到最大的三个区域
    blocks = []
    for c in contours:
        print(c)
        # 找出轮廓的左上和右下点，计算出其面积和长宽比
        r = find_retangle(c)
        a = (r[2] - r[0]) * (r[3] - r[1])
        s = (r[2] - r[0]) / (r[3] - r[1])

        blocks.append([r, a, s])

    # 选出面积最大的3个区域
    blocks = sorted(blocks, key=lambda b: b[2])[-3:]

    # 使用颜色识别判断出最像车牌的区域
    maxweight, maxinedx = 0, -1

    for i in range(len(blocks)):
        b = orgimg[blocks[i][0][1]:blocks[i][0][3], blocks[i][0][0]:blocks[i][0][2]]
        # RGB 转HSV
        hsv = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)

        # 蓝色车牌范围
        lower = np.array([100, 50, 50])
        upper = np.array([140, 255, 255])

        # 根据阈值构建掩膜
        mask = cv2.inRange(hsv, lower, upper)

        # 统计权值
        w1 = 0
        for m in mask:
            w1 += m / 255

        w2 = 0
        for w in w1:
            w2 += w

        # 选出最大权值的区域
        if w2 > maxweight:
            maxindex = i
            maxweight = w2

    return blocks[maxindex][0]
    print(contours)


def find_license(img):
    '''预处理'''
    # 压缩图像
    a = 400 * img.shape[0] / img.shape[1]
    a = int(a)
    img = cv2.resize(img, (400, a))
    cv2.imshow('img',img)
    cv2.waitKey()

    # RGB转灰色
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayimg', grayimg)
    cv2.waitKey()

    # 灰度拉伸
    stretchedimg = stretch(grayimg)
    cv2.imshow('stretchedimg', stretchedimg)
    cv2.waitKey()

    # 进行开运算，用来去除噪声
    r = 16
    h = w = r * 2 + 1
    kernel = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(kernel, (r, r), r, 1, -1)
    openingimg = cv2.morphologyEx(stretchedimg, cv2.MORPH_OPEN, kernel)
    cv2.imshow('openingimg', openingimg)
    cv2.waitKey()

    strtimg = cv2.absdiff(stretchedimg, openingimg)
    cv2.imshow('strtimg', strtimg)
    cv2.waitKey()

    # 图像二值化
    binaryimg = dobinaryzation(strtimg)
    cv2.imshow('binaryimg', binaryimg)
    cv2.waitKey()

    # Canny算子进行边缘检测
    cannyimg = cv2.Canny(binaryimg, binaryimg.shape[0], binaryimg.shape[1])
    cv2.imshow('cannyimg', cannyimg)
    cv2.waitKey()

    '''消除小区域，连通大区域'''
    # 进行闭运算
    kernel = np.ones((5, 19), np.uint8)
    closingimg = cv2.morphologyEx(cannyimg, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closingimg', closingimg)
    cv2.waitKey()

    # 进行开运算
    openingimg = cv2.morphologyEx(closingimg, cv2.MORPH_OPEN, kernel)
    cv2.imshow('openingimg', openingimg)
    cv2.waitKey()

    # 再次进行开运算
    kernel = np.ones((11, 5), np.uint8)
    openingimg = cv2.morphologyEx(openingimg, cv2.MORPH_OPEN, kernel)
    print(openingimg.shape)
    cv2.imshow('openingimg', openingimg)
    cv2.waitKey()

    # 消除小区域，定位车牌位置
    rect = locate_license(openingimg, img)
    return rect, img


if __name__ == '__main__':
    orgimg = cv2.imread('imgs/fire/t00001.jpg')
    rect, img = find_license(orgimg)

    cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    cv2.imshow('img', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
