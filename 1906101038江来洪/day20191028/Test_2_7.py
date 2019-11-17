#产生每位数字相同的n位数
A,B = map(int,input('请输入两个数字：').split(','))
for i in range(B):
    if i < B:
        print(A,end='')
