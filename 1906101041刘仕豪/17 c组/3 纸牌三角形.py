num_list = [1,2,3,4,5,6,7,8,9]
cnt = 0
# line1 = num_list[0]+num_list[1]+num_list[3]+num_list[5]
# line2 = num_list[0]+num_list[2]+num_list[4]+num_list[8]
# line3 = num_list[5]+num_list[6]+num_list[7]+num_list[8]
def perm(l):
    if(len(l)<=1):
        return [l]
    r=[]
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r
all_list = perm(num_list)
for i in all_list:
    if i[0]+i[1]+i[3]+i[5] == i[0]+i[2]+i[4]+i[8] and i[0]+i[2]+i[4]+i[8] == i[5]+i[6]+i[7]+i[8]:
        cnt += 1
print(int(cnt/6))