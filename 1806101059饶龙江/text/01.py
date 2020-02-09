import PIL as IMAGE

file_src='img processing/imgs/fire/T0t0.jpg'#需要压缩的图片地址
img_src='img processing/imgs/fire/yasuo.jpg'#压缩后的图片地址
img = IMAGE.open(file_src)
w,h = img.size
w,h = round(w * 0.2),round(h * 0.2)		# 去掉浮点，防报错

img = img.resize((w,h), IMAGE.ANTIALIAS)
img.save(img_src, optimize=True, quality=85)#	 质量为85效果最好