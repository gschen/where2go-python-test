A,B=map(int,input().split())
if A>=5:
    if B<=40:
        s = B*50
    else:
        s = 2000+(B-40)*75
else:
    if B<=40:
        s = B*30
    else:
        s = 1200+(B-40)*45
print("%.2f" %s)
