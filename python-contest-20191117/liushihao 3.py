# s = input()
# for i in s:
#     if i == '-':
#         a = s[s.index(i) - 4:s.index(i)]
#         b = s[s.index(i):s.index(i)+2]
#         if int(a) <= 2019 and int(a) >= 1979 and int(b) >= 0 and int(b) <= 12:
#             print(s.index(i)-4)
str = input()
list1 = [x for x in range(1979,2020)]
list2 = ['01','02','03','04','05','06','07','08','09','10','11','12']
for i in str:
    if i == '-':
        a = str.index(i)
        b = int(''.join(str[a-4:a]))
        c = ''.join(str[a+1:a+3])
        if b in list1 and c in list2:
            print(a-3)
