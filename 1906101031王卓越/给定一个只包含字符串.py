def raw(n):
    n=str(n)
    k=0
    for i in range(0,len(n)):
        if n[k]==n[-k-1]:
            print("true")
            k=k+2
        elif n[k]!=n[-k-1]:
            print("false")
            k=k+2
        elif n[k]!=n[k+1]:
            print("true")
            k=k+2
        elif n[k]!=n[k+1]:
            print("false")
            k=k+2
    return
print(raw('()[]{}'))