'''
809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
求??代表的两位数，及809*??后的结果。
'''
for i in range(10,100):
    if 1000<809*i<9999 and 10<8*i<99 and 100<9*i<999:
        print('??代表的两位数为{}，809*??的结果为{}。'.format(i,i*809))