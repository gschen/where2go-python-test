import os
with open((os.path.join('D:\\python\\wuyichen.txt')), 'r',encoding='UTF-8') as f:
	data = f.read()
strlist = data.split('md5=')
#for item in strlist[1:]:
#	try:
#		list_link = item.split(' target=_blank')[0]
#		print(list_link)
#	except:
#		pass
print(strlist)
