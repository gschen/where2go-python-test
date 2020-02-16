# 2.标题：李白打酒

#     话说大诗人李白，一生好饮。幸好他从不开车。

#     一天，他提着酒壶，从家里出来，酒壶中有酒2斗。他边走边唱：

#     无事街上走，提壶去打酒。
#     逢店加一倍，遇花喝一斗。

#     这一路上，他一共遇到店5次，遇到花10次，已知最后一次遇到的是花，他正好把酒喝光了。 

#     请你计算李白遇到店和花的次序，可以把遇店记为a，遇花记为b。则：babaabbabbabbbb 就是合理的次序。像这样的答案一共有多少呢？请你计算出所有可能方案的个数（包含题目给出的）。

#     注意：通过浏览器提交答案。答案是个整数。不要书写任何多余的内容。
num=2
sum=0
for num1 in range(num):
    k1=num1
    num1=(num-num1)*2
    n1=num1-num+k1
    for num2 in range(num1):
        k2=num2
        num2=(num1-num2)*2
        n2=num2-num1+k2
        for num3 in range(num2):
            k3=num3
            num3=(num2-num3)*2
            n3=num3-num2+k3
            for num4 in range(num3):
                k4=num4
                num4=(num3-num4)*2
                n4=num4-num3+k4
                for num5 in range(num4):
                    k5=num5
                    num5=(num4-num5)*2
                    n5=num5-num4+k5
                    k6=num5
                    if n1+n2+n3+n4+n5==8 and num5!=0 and k1+k2+k3+k4+k5+k6==10:
                        sum+=1
print(sum)



