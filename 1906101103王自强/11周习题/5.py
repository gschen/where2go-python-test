'''5.	给定任意一张RGB三通道图片，分别求其RGB三通道均值，并打印'''
from PIL import Image
im = Image.open("QQ20191110175143.jpg")
pix = im.load()
width = im.size[0]
height = im.size[1]
RZ,GZ,BZ=0,0,0
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        RZ+=r
        GZ+=g
        BZ+=b
times=width*height
RJ=RZ/times
GJ=GZ/times
BJ=BZ/times
print(RJ,GJ,BJ)