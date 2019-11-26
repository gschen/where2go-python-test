for b in range(4):
    i = False
    while i==False:
        name=input("用户名:")
        password=input("密码:")
        while name == "王卓越" and password == "123":
            print("登陆成功")
         #   print(i=True)
        else:
            print("登陆失败")
            print("你还剩%d次机会" % (3-b))
            break
else:
    print("你已经输入错误超过四次请重新输入")
    

 