'''
方程ax2+bx+c=0，输入方程的系数a、b、c，输出其根的情况。
输入说明：三个实数a,b,c分别对应二次项、一次项和0次项的系数；
输出说明：方程根的情况，是下列五种情况之一：无解、无穷解、一次方程解、二次方程实数解和二次方程复数解，分别对应输出为1，2，3，4，5。
输入样例：1 -2 1
输出样例：4
'''

def jiefangchen(a, b, c):
    if a == 0 and b == 0 and c != 0:
        print(1)
    elif a == 0 and b == 0 and c == 0:
        print(2)
    elif a == 0:
        print(3)
    elif b*b - 4*a*c >= 0:
        print(4)
    elif b*b - 4*a*c < 0:
        print(5)


jiefangchen(1, -2, 1)
