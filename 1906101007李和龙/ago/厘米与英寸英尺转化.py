cm = int(input())
inch = (cm / 0.3048 / 100) * 12

foot = 0
aaa = True
while aaa == True:
    if inch >= 12:
        foot += 1
        inch = inch - 12
    if inch < 12:
        aaa = False

print(foot, "foot", int(inch), "inch")  # int取整




