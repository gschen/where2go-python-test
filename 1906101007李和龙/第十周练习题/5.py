"""
 5、	809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数
   ，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
"""

for i in range(10,100):
    i = int(i)
    if 809*i == 800*i+9*i:
        #print(i)
        if len(str(int(809*i)))==4 and len(str(int(8*i))) == 2 and len(str(int(9*i))) == 3:
            print(i)
            print(809*i)
            # print(8*i)
            # print(9*i)