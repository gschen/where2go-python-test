# (1)
import random
for i in range(10):
    print(random.randint(0,100))
# (2)
import random
a = random.randint(0,49)
b = a*2+1
print(b)

# (3)
import random
a = 'abcdefghij'
for i in range(4):
    print(random.choice(a))

# (4)
import random
a = ['apple','pear','peach','orange']
print(random.choice(a))