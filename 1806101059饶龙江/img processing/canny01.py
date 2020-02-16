import cv2 as cv
import  numpy as np
import math


def find_retangle(contour):
    y, x = [], []

    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])

    return [min(y), min(x), max(y), max(x)]


def locate_license(img, orgimg):
    img, contours, hierachy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # 找到最大的三个区域
    blocks = []
    for c in contours:
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
        hsv = cv.cvtColor(b, cv.COLOR_BGR2HSV)

        # 蓝色车牌范围
        lower = np.array([100, 50, 50])
        upper = np.array([140, 255, 255])

        # 根据阈值构建掩膜
        mask = cv.inRange(hsv, lower, upper)

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

def CANNY(img_path):
    # 读取图片
    img = cv.imread(img_path)
    print('-----',img.shape)
    print(img[1][2])
    # BGR 转换成 RGB 格式
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # 灰度化
    img_gray = np.dot(img_rgb[..., :3], [0.299, 0.587, 0.114])
    #高斯滤波器
    #二值化
    max = float(img.max())
    min = float(img.min())

    x = max - ((max - min) / 2)
    ret,img_gray = cv.threshold(img_gray, x, 255, cv.THRESH_BINARY)
    sigma1 = sigma2 = 1#设置方差
    gau_sum = 0
    gaussian = np.zeros([5, 5])
    for i in range(5):
        for j in range(5):
            gaussian[i, j] = math.exp((-1 / (2 * sigma1 * sigma2)) * (np.square(i - 3) + np.square(j - 3))) / (
                        2 * math.pi * sigma1 * sigma2)
            gau_sum = gau_sum + gaussian[i, j]
    # 归一化处理
    gaussian = gaussian / gau_sum
    # 高斯滤波
    W, H = img_gray.shape
    new_gray = np.zeros([W - 5, H - 5])
    for i in range(W - 5):
        for j in range(H - 5):
            new_gray[i, j] = np.sum(img_gray[i:i + 5, j:j + 5] * gaussian)#采用卷积的方法
    cv.imshow("new_gray",new_gray)
    # 计算梯度幅值
    W, H = new_gray.shape
    #由于涉及到边界的问题，所以创建的新数组比原数组要少2行2列
    dx = np.zeros([W - 1, H - 1])
    dy = np.zeros([W - 1, H - 1])
    M = np.zeros([W - 1, H - 1])
    theta = np.zeros([W - 1, H - 1])
    #使用微差代替微商
    '''
    for i in range(W - 1):
        for j in range(H - 1):
            dx[i, j] = new_gray[i + 1, j] - new_gray[i, j]
            dy[i, j] = new_gray[i, j + 1] - new_gray[i, j]
            # 图像梯度幅值作为图像强度值
            M[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))
            # 计算  θ - artan(dx/dy)
            theta[i, j] = math.atan(dx[i, j] / (dy[i, j] + 0.000000001))
    '''


    #使用soble算子
    soble_X = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # X方向
    soble_Y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # Y方向
    for i in range(W-2):
        for j in range(H-2):
            dx[i][j] = np.sum(new_gray[i:i + 3, j:j + 3] * soble_X)
            dy[i][j] = np.sum(new_gray[i:i + 3, j:j + 3] * soble_Y)
            M[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))


    '''
    #使用robert算子

    robert = np.array([[-1,-1],[1,1]])
    for i in range(W-1):
        for j in range(H-1):
            dx[i][j] = np.sum(new_gray[i:i+2,j:j+2]*robert)
            dy[i][j] = np.sum(new_gray[i:i+2,j:j+2]*robert)
            M[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))
    '''
    '''
    #使用laplace算子
    laplace1 =np.array([[0,1,0],[1,-4,1],[0,1,0]])#第一种laplace算子
    laplace2 = np.array([[0,1,0],[1,-4,1],[0,1,0]])#第二种laplace算子
    for i in range(W-2):
        for j in range(H-2):
            dx[i,j] = np.sum(new_gray[i:i+3,j:j+3]*laplace1)
            dy[i,j] = np.sum(new_gray[i:i+3,j:j+3]*laplace1)
            #dx[i,j] = np.sum(new_gray[i:i+3,j:j+3]*laplace2)
            #dy[i,j] = np.sum(new_gray[i:i+3,j:j+3]*laplace2)
            M[i,j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))
     '''
    #极大值抑制
    d = np.copy(M)
    W, H = M.shape
    NMS = np.copy(d)
    NMS[0, :] = NMS[W - 1, :] = NMS[:, 0] = NMS[:, H - 1] = 0
    for i in range(1, W - 1):
        for j in range(1, H - 1):
            # 如果当前梯度为0，该点就不是边缘点
            if M[i, j] == 0:
                NMS[i, j] = 0
            else:
                gradX = dx[i, j]  # 当前点 x 方向导数
                gradY = dy[i, j]  # 当前点 y 方向导数
                gradTemp = d[i, j]  # 当前梯度点
                # 如果 y 方向梯度值比较大，说明导数方向趋向于 y 分量
                if np.abs(gradY) > np.abs(gradX):
                    weight = np.abs(gradX) / np.abs(gradY)  # 权重
                    grad2 = d[i - 1, j]
                    grad4 = d[i + 1, j]
                    # 如果 x, y 方向导数符号一致
                    # 像素点位置关系
                    # g1 g2
                    #    g
                    #    g4 g3
                    if gradX * gradY > 0:
                        grad1 = d[i - 1, j - 1]
                        grad3 = d[i + 1, j + 1]
                    # 如果 x，y 方向导数符号相反
                    # 像素点位置关系
                    #    g2 g1
                    #    g
                    # g3 g4
                    else:
                        grad1 = d[i - 1, j + 1]
                        grad3 = d[i + 1, j - 1]
                # 如果 x 方向梯度值比较大
                else:
                    weight = np.abs(gradY) / np.abs(gradX)
                    grad2 = d[i, j - 1]
                    grad4 = d[i, j + 1]
                    # 如果 x, y 方向导数符号一致
                    # 像素点位置关系
                    #      g3
                    # g2 g g4
                    # g1
                    if gradX * gradY > 0:
                        grad1 = d[i + 1, j - 1]
                        grad3 = d[i - 1, j + 1]
                    # 如果 x，y 方向导数符号相反
                    # 像素点位置关系
                    # g1
                    # g2 g g4
                    #      g3
                    else:
                        grad1 = d[i - 1, j - 1]
                        grad3 = d[i + 1, j + 1]
                # 利用 grad1-grad4 对梯度进行插值
                gradTemp1 = weight * grad1 + (1 - weight) * grad2
                gradTemp2 = weight * grad3 + (1 - weight) * grad4
                # 当前像素的梯度是局部的最大值，可能是边缘点
                if gradTemp >= gradTemp1 and gradTemp >= gradTemp2:
                    NMS[i, j] = gradTemp
                else:
                    # 不可能是边缘点
                    NMS[i, j] = 0
    W, H = NMS.shape
    DT = np.zeros([W, H])
    # 定义高低阈值
    TL = 0.1 * np.max(NMS)
    TH = 0.3 * np.max(NMS)
    for i in range(1, W - 1):
        for j in range(1, H - 1):
            # 双阈值选取
            if (NMS[i, j] < TL):
                DT[i, j] = 0
            elif (NMS[i, j] > TH):
                DT[i, j] = 255
            # 连接
            elif (NMS[i - 1, j - 1:j + 1] < TH).any() or (NMS[i + 1, j - 1:j + 1].any() or (NMS[i, [j - 1, j + 1]] < TH).any()):
                DT[i, j] = 255

    kernel = np.ones((5, 20), np.uint8)
    closingimg = cv.morphologyEx(DT, cv.MORPH_CLOSE, kernel)
    cv.imshow('closingimg', closingimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 进行开运算
    openingimg = cv.morphologyEx(closingimg, cv.MORPH_OPEN, kernel)
    cv.imshow('openingimg', openingimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 再次进行开运算
    kernel = np.ones((11, 5), np.uint8)
    openingimg = cv.morphologyEx(openingimg, cv.MORPH_OPEN, kernel)
    cv.imshow('openingimg', openingimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    rect = locate_license(openingimg, img)
    return rect, img
    #通过轮廓和颜色判断车牌区域,想法：通过颜色特征结合轮廓特征找到车牌区域。
    '''
    lower = np.array([100, 50, 50])
    upper = np.array([140, 255, 255])
    lis1=[]
    lis2=[]
    for i in range(len(openingimg)):
        for j in range(len(openingimg[i])):
            if 100<img[i][j][0]<140 and 50<img[i][j][1]<255 and 50<img[i][j][0]<255 and openingimg[i][j]==255:
                lis1.append(i)
                lis2.append(j)
    print("------", lis1)
    print("------", lis2)
    chepaiquyu=img[lis1[0]:lis1[-1],lis2[0]:lis2[-1]]
    cv.imshow("----",chepaiquyu)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''








    '''
    #寻找轮廓
    image, contours, hierarchy = cv.findContours(openingimg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('imageshow', image)
    #绘制轮廓
    contours_img = cv.drawContours(openingimg, contours, -1, (0, 255, 0),5)  # img为三通道才能显示轮廓
    cv.imshow('drawimg', contours_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''


CANNY("imgs/fire/u=1463018956,861119745&fm=26&gp=0.jpg")

