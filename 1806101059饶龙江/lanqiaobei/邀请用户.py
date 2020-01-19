n=int(input())
def day(n):
    people=[]
    if n<=7:
        return  0
    else:
        r = list(range(n-7,0,-3))
        for i in r:
            people.append(day(i))
        return len(r)+sum(people)
print(day(n)+1)

