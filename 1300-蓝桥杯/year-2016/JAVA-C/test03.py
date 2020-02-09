import sys

sys.setrecursionlimit(3000) # 设置最大递归深度为3000

history=[]
def test(x,max_val,history=history):

    history.append(x)
    if x==1 :
        print(max_val)
        return max_val
    x=str(x)
    #print('测试',x,max_val)
    new_x=0
    for i in x:
        new_x+=eval(i)**2
    if new_x>max_val:
        max_val=new_x

    if new_x in history:
        print(max_val)
        return max_val
    else:
        test(new_x,max_val)
test(12,0)
