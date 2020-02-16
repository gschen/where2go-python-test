n=int(input())
lis=[0]
li=[]
num1=0
num2=0
while True:
    if n==1:
        print(lis)
        break
    num1-=1
    num2+=1
    lis.append(num1)
    lis.append(num2)
    if len(lis)==n and sum(lis)==0:
        print(lis)
        break
    if len(lis)>n:
        lis.remove(0)
        if sum(lis)==0:
            print(lis)
            break
            



            




