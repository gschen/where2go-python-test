'''5、	809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，
8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，
及809*??后的结果。'''
for x in range(10,100):
    i=809*x
    j=8*x
    k=9*x
    if i==100*j+k and i in range(1000,10000)and j in range(10,100)and k in range(100,1000):
        print('??代表{}，829*？？结果为{}'.format(x,i))