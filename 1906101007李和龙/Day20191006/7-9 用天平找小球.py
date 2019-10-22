a,b,c = map(int,input().split())
if a == b and b != c:
    print("C")
if a == c and c != b:
    print("B")
if b == c and c != a:
    print("A")