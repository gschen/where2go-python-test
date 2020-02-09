for i in range(10,22):

    #满足4位数(x**3)不相同
    if len(set(str(i**3)))  == 4 and len(str(i**3))==4:

        # 满足6位数(x**4)不相同
        if len(set(str(i**4))) == 6 and len(str(i**4))==6:
            zifu=str(i**3)+str(i**4)

            # 满足10位数不相同
            if len(set(zifu))==10:

                print(i)