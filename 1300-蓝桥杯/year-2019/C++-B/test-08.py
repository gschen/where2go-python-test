N = int(input())
list1 = sorted(list(map(int, input().split())))
list2 = []

def gcd(numList):
    listAll = []
    for i in numList:
        One = set()
        for j in range(1, i + 1):
            if i % j == 0:
                One.add(j)
        listAll.append(One)

    for i in range(len(listAll)):
        end = listAll[0]
        end = end & listAll[i]

    return max(end)

is_arithmetic_progression = 0

for i in range(N - 1):
    if list1[i + 1] - list1[i] == 0:
        is_arithmetic_progression = 1
    list2.append(list1[i + 1] - list1[i])

if is_arithmetic_progression == 1:
    print(N)
else:
    gcd = gcd(list2)
    min = list1[0]
    max = list1[-1]
    ans = int((max - min) / gcd + 1)
    print(ans)
