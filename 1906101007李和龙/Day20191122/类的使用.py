class A(object):
    bar = 1
a = A()     #a是A的实例
print(getattr(a, 'bar'))       # 获取属性 bar 值

# getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常

print(getattr(a, 'bar2', "3"))    # 属性 bar2 不存在，但设置了默认值

setattr(a,"k",6)                #新增属性  k值
print(getattr(a,"k"))
print(a.k)


# delattr(a,"k")                  #删除 属性 k 值
# print(getattr(a,"k"))
