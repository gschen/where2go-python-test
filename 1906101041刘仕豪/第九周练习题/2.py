'''
2、	一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
import math
for a in range(1,1000):
    if int(math.sqrt(a+100))*int(math.sqrt(a+100))==a+100 and int(math.sqrt(a+168))*int(math.sqrt(a+168))==a+168:
        print("该数为：{}".format(a))
