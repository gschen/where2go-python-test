# 2
import random
b = 2
while b==2:
    a = random.randint(0,100)
    if a%2!=0:
        break
print(a)

# 3
import random
a = 'abcdefghij'
for i in range(4):
    print(random.choice(a))

#4
import random
a = ['apple','pear','peach','orange']
print(random.choice(a))