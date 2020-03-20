count = 0

def panduan(n):
    a = []
    for i in str(n):
        a.append(i)
    if '2' in a:
        return 0
    if '4' in a:
        return 0
    else:
        return 1

for i in range(1,2019):
    for j in range(i,2019):
        k = 2019 - i - j
        if k > 0 and k >= j:
            if panduan(i) == 1 and panduan(j) == 1 and panduan(k) == 1:
                count += 1
                print(i, ",", j, ",", k)
print(count)