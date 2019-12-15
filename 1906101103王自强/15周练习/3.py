N=int(input())
sum=0
for i in range(1,N+1):
    sum+=(i/2*i+1)*(-1)**(i-1)
print('sum=%.3f'%sum)