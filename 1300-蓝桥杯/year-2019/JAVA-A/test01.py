#01
sum_val=0
for i in range(1,2020):
    if '2' in str(i) or '0' in str(i) or '1' in str(i) or '9' in str(i):
        sum_val+=i**2
print(sum_val)