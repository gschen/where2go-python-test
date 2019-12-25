def Josephus_problem(num,gap):
    location_list = [a for a in range(1,num+1)]
    if num ==   1 :
        return
    else:
        index = 0
        for i in range(num-1):
            index = (index + gap )%len(location_list) - 1
            print("本次出局的人为：",location_list[index])
            del location_list[index]
            if index == 0:
                index = 0
        print( "最后剩下的为：",location_list[0])

Josephus_problem(5,3)
