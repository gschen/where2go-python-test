'''
第三题：复数幂
'''
A=2
B=3
a=2
b=3
for i in range(123456):
    A,B=A*a-B*b,A*b+a*B
if B>0:
    print("{}+{}i".format(A,B))
elif B==0:
    print(A)
else:
    print("{}{}i".format(A,B))