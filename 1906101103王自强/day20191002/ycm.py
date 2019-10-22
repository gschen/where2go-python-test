import random
times=100000
change_choice=0
no_change_choice=0
for i in range(times):
    car_indoor=random.randint(0,2)
    guess=random.randint(0,2)
    if car_indoor==guess:
        no_change_choice+=1
    else:
        change_choice+=1
print('不改选择：%f'%(no_change_choice/times))
print('更改选择：%f'%(change_choice/times))