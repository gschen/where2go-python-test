'''5.	给定任意一张RGB三通道图片，分别求其RGB三通道均值，并打印'''
from PIL import Image
im = Image.open("QQ20191110175143.jpg")#加载图片
pix = im.load()#求某点的rgb值
width = im.size[0]#求图片宽度
height = im.size[1]#求图片高度
RZ,GZ,BZ=0,0,0#初始值用于求和
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]#每一点的rgb值
        RZ+=r
        GZ+=g
        BZ+=b
times=width*height
RJ=RZ/times
GJ=GZ/times
BJ=BZ/times
print(RJ,GJ,BJ)