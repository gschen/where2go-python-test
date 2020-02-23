'''
8.标题：分糖果
'''
def check(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=temp:
            return False
        else:
            continue
    return True

if __name__=="__main__":
    n=int(input())
    res=0
    arr=list(map(int,input().split()))
    while True:
        t=arr[0]
        for i in range(n-1):
            arr[i]-=arr[i]/2
            arr[i]+=arr[i+1]/2
            if arr[i]%2==1:
                arr[i]+=1
                res+=1
        arr[n-1]-=arr[n-1]/2
        arr[n-1]+=t/2
        if arr[n-1]%2==1:
            arr[n-1]+=1
            res+=1
        if check(arr):
            print(res)
            break