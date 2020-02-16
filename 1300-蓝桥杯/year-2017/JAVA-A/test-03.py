import random

g = [[5, 1, 1], [5, 1, 2], [5, 2, 1], [5, 2, 2], [6, 1, 1], [6, 1, 2], [6, 2, 1], [6, 2, 2]]
y = [[3, 1, 1], [3, 1, 2], [3, 2, 1], [3, 2, 2], [4, 1, 1], [4, 1, 2], [4, 2, 1], [4, 2, 2]]
# o = [[1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 1, 1], [2, 1, 2], [2, 2, 1], [2, 2, 2]]

def rx():
    for i in g, y:
        for j in i:
            if j[0] == 6:
                if j[1] == 1:
                    if j[2] == 1:
                        j[2] = 2
                    else:
                        j[1] = 2
                else:
                    if j[2] == 1:
                        j[1] = 1
                    else:
                        j[2] = 1

            elif j[0] != 5 and j[1] == 2:
                if j[0] != 4:
                    j[0] = j[0] + 1
                else:
                    j[0] = 1


def ry():
    for i in g, y:
        for j in i:
            if j[0] == 3:
                if j[1] == 1:
                    if j[2] == 1:
                        j[2] = 2
                    else:
                        j[1] = 2
                else:
                    if j[2] == 1:
                        j[1] = 1
                    else:
                        j[2] = 1

            elif j[0] != 1 and j[2] == 2:
                if j[0] == 6:
                    j[0] = 2
                elif j[0] == 2:
                    j[0] = 5
                elif j[0] == 5:
                    j[0] = 4
                else:
                    j[0] = 6


def rz():
    for i in g, y:
        for j in i:
            if j[0] == 2:
                if j[1] == 1:
                    if j[2] == 1:
                        j[2] = 2
                    else:
                        j[1] = 2
                else:
                    if j[2] == 1:
                        j[1] = 1
                    else:
                        j[2] = 1

            elif j[0] == 5:
                if j[1] == 2 and j[2] == 1:
                    j[0] = 3
                    j[1] = 1
                elif j[1] == 2 and j[2] == 2:
                    j[0] = 3
                    j[2] = 1

            elif j[0] == 3:
                if j[1] == 1 and j[2] == 1:
                    j[0] = 6
                    j[2] = 2
                elif j[1] == 2 and j[2] == 1:
                    j[0] = 6
                    j[1] = 1

            elif j[0] == 6:
                if j[1] == 1 and j[2] == 2:
                    j[0] = 1
                    j[1] = 2
                elif j[1] == 1 and j[2] == 1:
                    j[0] = 1
                    j[2] = 2

            else:
                if j[1] == 1 and j[2] == 2:
                    j[0] = 5
                    j[1] = 2
                elif j[1] == 2 and j[2] == 2:
                    j[0] = 5
                    j[2] = 1



def run(num):
    all = [[sorted(g),sorted(y)]]
    for i in range(num):
        nums=random.randint(0, 2)
        if nums == 0:
            rx()
        elif nums == 1:
            ry()
        else:
            rz()
        for a in all:
            if a == [sorted(g),sorted(y)]:
                continue
        all.append([sorted(g),sorted(y)])
    print(len(all))
run(1000)

# print("green :", g)
# print("yellow:", y)
# print("orange:", o)
