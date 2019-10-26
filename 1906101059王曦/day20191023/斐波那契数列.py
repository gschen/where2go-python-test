i = eval(input("请输入第几项："))
list = [0,1]
n = 2
while True:
    list.append(list[-1]+list[-2])
    n = n+1
    if n == i:
        print(list[-1])
        break