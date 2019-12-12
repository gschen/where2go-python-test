x=float(input())
if x<=50:
    print('%.2f' % x*0.53)
if x>50:
    print('%.2f' % (x-50)*0.58+50*0.53)