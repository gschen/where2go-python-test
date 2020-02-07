s = "abcde"
maxLetters = 2
minSize = 3
maxSize = 3
maxl = []
if maxSize != minSize:
    for x in range(minSize, maxSize + 1):
        for y in range(len(s)):
            if y + x < len(s) + 1:
                maxl.append(s[y:y + x])
if maxSize == minSize:
    for y in range(len(s)):
        if y + minSize < len(s) + 1:
            maxl.append(s[y:y + minSize])

i=-1
while len(maxl)>0:
    i=i+1
    if len(set(maxl[i])) > maxLetters:
        del maxl[i]
        i=i-1
dict = {}
for key in maxl:
    dict[key] = dict.get(key, 0) + 1
if not bool(dict):
    print(0)
else:
    print(max(dict.values()))
