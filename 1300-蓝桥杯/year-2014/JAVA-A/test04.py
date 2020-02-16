'''
4.标题：六角填数
'''
ls_a=[2,4,5,6,7,9,10,11,12]
def full_num(step):
    if step==len(ls_a):
        judge()
        return
    for i in range(step,len(ls_a)):
        tmp=ls_a[i]
        ls_a[i]=ls_a[step]
        ls_a[step]=tmp
        full_num(step+1)
        tmp=ls_a[i]
        ls_a[i]=ls_a[step]
        ls_a[step]=tmp

def judge():
    roud1=1+ls_a[0]+ls_a[8]+ls_a[7]
    roud2 = 1 + ls_a[1] + ls_a[3] + ls_a[4]
    roud3 = 8 + ls_a[0] + ls_a[1] + ls_a[2]
    roud4 = 8 + ls_a[8] + ls_a[6] + 3
    roud5 = ls_a[2] + ls_a[3] + ls_a[5] + 3
    roud6 = ls_a[7] + ls_a[6] + ls_a[5] + ls_a[4]
    if roud1==roud2 and roud2==roud3 and roud3==roud4 and roud4==roud5 and roud5==roud6:
        print(ls_a[8])
if __name__=="__main__":

    full_num(0)