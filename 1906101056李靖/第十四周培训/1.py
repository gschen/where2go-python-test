def my_chengji(x):
    if x==1:
        return 1
    return x*my_chengji(x-1)
print(my_chengji(100))