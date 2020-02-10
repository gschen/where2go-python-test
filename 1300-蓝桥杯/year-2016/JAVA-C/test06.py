def main(x,max_x):
    if x>max_x:
        max_x=x
    if x<=1:
        print(int(max_x))
        return int(max_x)
    elif x%2==0:
        x=x/2
        main(x,max_x)
    else:
        x=x*3+1
        main(x, max_x)
main(9,9)