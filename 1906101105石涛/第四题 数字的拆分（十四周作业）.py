# coding=utf-8
1,2,5,11
x=int(input('请输入一个你比较喜欢的正整数：'))
print()
print('准备好了吗？我要开拆了哈，嘿嘿...')
while x>=11:
    x=x-11
    print(11)
while x>=5:
    x=x-5
    print(5)
while x>=2:
    x=x-2
    print(2)
if x==1:
    print(1)