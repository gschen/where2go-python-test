A=int(input('球A'))
B=int(input('球B'))
C=int(input('球C'))
if A==B and C!=A and C!=B:
    print('C')
if A==C and B!=A and B!=C:
    print('B')
if B==C and A!=B and A!=C:
    print('A')





