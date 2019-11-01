'''
4、	找到年龄最大的人，并输出。字典“{"li":18,"wang":50,"zhang":20,"sun":22}”
'''
d = {"li":18,"wang":50,"zhang":20,"sun":22}
def max():
    age = 0
    for key, value in dict.items():
        if value>age:
            age=value
            name=key
    print('年龄最大的人为{}岁的{}'.format(age,name))
max(d)