#100米高小球落地反弹10次。
n = 1
H = 100
s = 0
while n<=10:
    s = (3/2)*H+s
    H = H/2
    n += 1
print('经过10次后小球总共走了%f米，第10次小球反弹%f米高' % (s,H))
