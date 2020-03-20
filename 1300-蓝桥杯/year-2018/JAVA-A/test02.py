'''
第二题：星期一
'''
import datetime
a=datetime.date(1901,1,1)
b=datetime.date(2000,12,31)
sum=(b.__sub__(a).days+1)//7
print(sum)
