'''
13、	一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

a = int(input("请输入您的五位数："))
wan=a//10000
qian=(a-wan*10000)//1000
bai=(a-wan*10000-qian*1000)//100
shi=(a-wan*10000-qian*1000-bai*100)//10
ge=a-wan*10000-qian*1000-bai*100-shi*10
if wan==ge and qian==shi:
    print("该数为回文数")
else:
    print("该数不为回文数")