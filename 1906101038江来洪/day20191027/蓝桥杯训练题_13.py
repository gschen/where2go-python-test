#判断一个五位数是不是回文数
x = int(input('请输入一个五位数：'))
a = x//10000
b = x//1000%10
c = x//100%10
d = x//10%10
e = x%10
if a==e and b==d:
    print('该数是回文数')
else:
    print('该数不是回文数')