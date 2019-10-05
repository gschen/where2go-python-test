from prettytable import PrettyTable
lower,upper=map(int,input().split())
if lower >= upper or upper >= 100:
    print('Invalid')
else:
    a = PrettyTable(['fahr','celsius'])
    while lower <= upper:
        C = 5 * (lower - 32) / 9
        a.add_row(['{}'.format(lower),'{:.1f}'.format(C)])
        lower += 2
        a.align['fahr']='l'
        a.align['celsius']='l'
    print(a)