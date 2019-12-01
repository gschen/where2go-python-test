"""方程ax2+bx+c=0,输入方程的系数a、b、C,输出其根的情况。输入说明:三个实数a,b,c分别对应二二次项、
一-次项和0次项的系数;
输出说明:方程根的情况，是下列五种情况之一:无解、无穷解、- -次方程解、
二次方程实数解和二次方程复数解，分别对应输出为1, 2, 3, 4, 5。输入样例:
1 -21输出样例: 4
"""
def jiang(a,b,c):
    if a == 0:
        if b == 0:
            if c != 0:
                return 1
            else:
                return 2
        else:
            return 3
    else:
        if b**2-4*a*c >= 0:
            return 4
        else:
            return 5
a,b,c = map(int,input().split())
print(jiang(a,b,c))