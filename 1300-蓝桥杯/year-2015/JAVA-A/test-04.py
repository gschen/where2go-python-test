s=[x for x in range(1,50)]
for i in range(0,46):
    for j in range(0,48):
        x=s[i]*s[i+1]
        y=s[j]*s[j+1]
        sum_number=x+y+1225-s[i]-s[j]-s[i+1]-s[j+1]
        if sum_number==2015:
            print(s[i],s[j])
