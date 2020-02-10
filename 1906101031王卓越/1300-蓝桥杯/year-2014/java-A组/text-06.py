# 6.标题：六角填数

#     如图【1.png】所示六角形中，填入1~12的数字。

#     使得每条直线上的数字之和都相同。

# 图中，已经替你填好了3个数字，请你计算星号位置所代表的数字是多少？
 

# 请通过浏览器提交答案，不要填写多余的内容。
li=list(range(1,13))
lis=[1,3,8]
for i in lis:
    li.remove(i)
for num1 in li:
    for num2 in li:
        for num3 in li:
            for num7 in li:
                for num8 in li:
                    for num4 in li:
                        for num5 in li:
                            if 8+num2+num4+num7==num1+num3+num5+num8  and num4!=num5 and  num1+num2-num3==10 and num1+num8-num7==10 and num1!=num2 and num1!=num3 and num1!=num4 and num1!=num5 and num1!=num7 and num1!=num8 and num2!=num3 and num2!=num4 and num2!=num5 and num2!=num7 and num2!=num8 and num3!=num4 and num3!=num5 and  num3!=num7 and num3!=num8 and num4!=num5 and num4!=num7 and num4!=num8 and num5!=num7 and num5!=num8 and num7!=num8 :
                                x=8+num2+num4+num7-11-num3
                                if x in li and x!=num1 and x!=num2 and x!=num3 and x!=num4 and x!=num5 and x!=num7 and x!=num8 :
                                    print(x)

