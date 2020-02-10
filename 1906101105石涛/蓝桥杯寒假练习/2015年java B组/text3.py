# coding=utf-8

'''
3.三羊献瑞
•	观察下面的加法算式：
      祥 瑞 生 辉  +   三 羊 献 瑞
----------------------------
   三 羊 生 瑞 气
•	其中，相同的汉字代表相同的数字，不同的汉字代表不同的数字。
•	请你填写“三羊献瑞”所代表的4位数字（答案唯一），不要填写任何多余内容。

'''
# (思路：由题可知道，“三”字只能为1，所以就可以去相应范围，然后把数字全部拆开，进行判断就可以了，还有就是他们有八个不同的数字)
from datetime import datetime
print(datetime.now())
for it in range(1000,2000):
    for i in range(9000,10000):
        m=i+it

        m1,m2,m3,m4,m5=m//10000,m//1000-m//10000*10,m//100-m//1000*10,m//10-m//100*10,m%10
        it1,it2,it3,it4=it//1000,it//100-it//1000*10,it//10-it//100*10,it%10
        i1,i2,i3,i4=i//1000,i//100-i//1000*10,i//10-i//100*10,i%10
        #或下面这种命名方式
        # m1,m2,m3,m4,m5=int(str(m)[0]),int(str(m)[1]),int(str(m)[2]),int(str(m)[3]),int(str(m)[4])
        # it1,it2,it3,it4=int(str(it)[0]),int(str(it)[1]),int(str(it)[2]),int(str(it)[3])
        # i1,i2,i3,i4=int(str(i)[0]),int(str(i)[1]),int(str(i)[2]),int(str(i)[3])

        l=set([m1,m2,m3,m4,m5,it1,it2,it3,it4,i1,i2,i3,i4])
        if m1==it1 and m2==it2 and m3==i3 and m4==it4 and m4==i2 and len(l)==8:
            print(it)
print(datetime.now())


'''其他人做的
似乎有点问题'''
#i祥，j瑞，k生，l辉，m三，n羊，o献
# print(datetime.now())

# for i in range(0,10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             for l in range(0, 10):
#                 for m in range(1, 10):
#                     for n in range(0, 10):
#                         for o in range(0,10):
#                             if i*1000+j*100+k*10+l+m*1000+n*100+o*10+j==m*10000+n*1000+k*100+j*10+(l+j)//10:
#                                 print(m,n,o,j)

# print(datetime.now())