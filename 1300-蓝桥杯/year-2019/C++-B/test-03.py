
def fib_loop(n):
  a, b ,c = 1, 1, 1
  for i in range(n + 1):
    a, b , c = b, c,a+b+c
  return a
for i in range(20190324):
    print(fib_loop(i)%10000,end=' ')

