a = '0100110001010001'
y = []
for i in range(1, len(a) + 1):  # 1,2,3,4

    for ii in range(len(a) - i + 1):
        x = a[ii:ii + i]
        y.append(x)
y = set(y)
print(len(y))
