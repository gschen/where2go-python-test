# 求100之内的素数。(素数：只能被1和本身整除的数)
def sushu(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
for i in range(1,101):
    sushu(i)
