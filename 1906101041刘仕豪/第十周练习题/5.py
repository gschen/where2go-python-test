'''
5、	809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
'''

for a in range(10,100):
    if 999<809*a<10000 and 9<8*a<100 and 99<9*a<1000 and 809*a==800*a+9*a:
        b=a*809
        print("??代表的两位数为{}，809*??后的结果为{}".format(a,b))
