from functools import*
def raw(x,y):
    return x+y
nums=list(eval(input()))
threshold=int(input())
for b in range(1,max(nums)*len(nums)):
    s=[]
    for a in nums:
        if a/b<=1:
            s.append(1)
        if a/b>1 and a%b!=0:
            s.append(int(a//b)+1)
        if a/b>1 and a%b==0:
            s.append(int(a/b))
    if int(reduce(raw,s))<=threshold:
        print(b)
        break


            

