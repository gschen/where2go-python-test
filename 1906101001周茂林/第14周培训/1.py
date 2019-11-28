'''
递归求阶乘
'''
def jiechen(x):

    if x == 1:
        return 1
    else:
        return x * jiechen(x-1)

print(jiechen(3))
