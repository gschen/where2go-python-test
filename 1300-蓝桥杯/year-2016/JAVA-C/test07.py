
def main(n):
    for a in range(n+1):
        for b in range(n + 1):
            for c in range(n + 1):
                for d in range(n + 1):
                    if a**2+b**2+c**2+d**2==n:
                        return a,b,c,d
print(main(12))