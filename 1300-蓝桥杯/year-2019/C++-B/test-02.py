ans=""
a=2019
abc="ZABCDEFGHIJKLMNOPQRSTUVWXY"
while 1:
    ans=abc[a%26]+ans
    a=a//26
    if a<1:
        break

print(ans)