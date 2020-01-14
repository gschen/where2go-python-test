n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
for i in nums:
    score = 0
    a = i//1000
    b = i%1000//100
    c = i%100//10
    d = i%10
    if a+1==b and b+1==c and c+1==d:
        score += 5
    if a-1==b and b-1==c and c-1==d:
        score += 5
    if a==b==c:
        score += 3
    if b==c==d:
        score += 3
    if a==b and c==d:
        score += 1
    if a==c and b==d:
        score += 1
    l = [a,b,c,d]
    ss = l.count(6)*1 + l.count(8)*1 + l.count(9)*1
    score += ss
    print(score)