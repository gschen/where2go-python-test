def sq(a,b,c):
    s = (a+b+c)/2
    d = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return d
s = sq(52.1,33.4,68.2)+sq(57.2,68.2,71.9)+sq(71.9,51.9,43.5)
print('%.2f'%s)