for i in range(3):
	name = input("用户名")
	password = input("密码")
	if name == "王卓越" and password == "123":
		print("登陆成功")
		break
	else:
		print("登陆失败")
		print("你还剩余%d次机会"%(2-i))