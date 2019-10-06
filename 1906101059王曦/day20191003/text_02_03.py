s = eval(input())
if s <=50:
    print("cost=%.2f" %(s*0.53))
else:
    print("cost=%.2f" %(50*0.53+(s-50)*(0.53+0.05)))