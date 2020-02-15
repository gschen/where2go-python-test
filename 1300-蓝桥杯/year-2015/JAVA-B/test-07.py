#骰子问题
n, m = input().split()
n=int(n)
lis1=[]
for i in range(eval(m)):
    lis = list(map(int, input().split()))
    lis1.append(lis)
print(lis1)
def touzi(n):
    #统计可以自由重叠的骰子组合
    sun_freedom=0
    for i in range(1,7):
        for j in lis1:
            if i not in j:
                sun_freedom+=1
    sum2=(4*6)**n
    return sum2
#统计无法自由组合的骰子组合
def sss(n):
    if n<=2:
        sum=1
        num = 0
        for i in range(1,7):
            if i==1:
                up=4
            elif i==2:
                up=5
            elif i==3:
                up=6
            elif i==4:
                up=1
            elif i==5:
                up=2
            else:
                up=3
            for j in lis1:
                if up not in j:
                    num+=1
            print(num)
        sum=sum*4*num
print(sss(n))














