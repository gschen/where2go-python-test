import cv2 as cv
import numpy as np

src = cv.imread("imgs/sc/test_3697.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#灰度化
