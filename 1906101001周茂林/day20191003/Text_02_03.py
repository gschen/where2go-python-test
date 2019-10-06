a = float(input())
if a < 0:
    print('Invalid Value')
elif a <= 50:
    print('cost = {:.2f}'.format(a * 0.53))
else:
    a = 50*0.53 + (a-50)*0.05
    print('cost = {:.2f}'.format(a))