#不同数据类型的格式化输出
x = input('请依次输入浮点数，整数，字符，浮点数：')
a,b,c,d = x.split()
a = float(a)
d = float(d)
print(c,b,'%.2f'% a,'%.2f'% d)