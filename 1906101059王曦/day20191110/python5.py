#求列表中最大最小
def finminamax(args):
    a = args[0]
    b = args[0]
    for i in args:
        if i > a:
            a = i
        if i < b:
            b = i
    print((a,b))





finminamax([23,-13,-4,-97,-21])