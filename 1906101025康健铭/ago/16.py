def add(x,y):
    return x+y


L = {'Jack':[90,80,70],'Machile':[80,60,30],'Bob':[80,70,90]}
for key,values in L.items():
    love = []
    love.append(values)
    from functools import reduce
    k = reduce(add,love)
print(k)

    
    
    
   
    
    



