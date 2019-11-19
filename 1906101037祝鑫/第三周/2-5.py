#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def jo(number):
    number = int(number)
    s = 0
    if number % 2 == 0:
        aa = 2
    else:
        aa = 1
    while aa != number:
        s += 1 / aa
        aa += 2
    print(s)