ans = 0
for a in range(1, 674):
    for b in range(a - 1, 1400):
        c = 2019 - a - b
        if a < b < c:
            right = 1
            for i in str(a), str(b), str(c):
                for j in i:
                    if j == '2' or j == '4':
                        right = 0

            if right == 1:
                ans += 1
print(ans)
