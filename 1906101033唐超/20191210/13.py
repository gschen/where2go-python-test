'''输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
温度转换的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。
输入格式:
在一行中输入2个整数，分别表示lower和upper的值，中间用空格分开。'''


lower,upper=map(int,input().split(" "))
if lower<=upper<=100:
    print("fahr celsius")
    for i in range(lower,upper,2):
        print('{} {:>6.1f}'.format(i,5*(i-32)/9))
else:
    print("Invalid")