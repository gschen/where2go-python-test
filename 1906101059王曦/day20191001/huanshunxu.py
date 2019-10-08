s = eval(input("请输入一个三位数："))
a = s//100;b = s-(a*100);c = b-((b//10)*10)
print(c*100+(b-c)+a)
