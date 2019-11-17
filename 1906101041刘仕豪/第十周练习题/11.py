'''
假设有两种微生物 X 和 Y
X出生后每隔3分钟分裂一次（数目加倍），Y出生后每隔2分钟分裂一次（数目加倍）。
一个新出生的X，半分钟之后吃掉1个Y，并且，从此开始，每隔1分钟吃1个Y。
现在已知有新出生的 X=10, Y=90，求60分钟后Y的数目。
'''

def shiyi(n):
    x=10
    y=90
    for t in range(1,n+1):
        y-=x
        if t%3==0:
            x=2*x
        if t%2==0:
            y=2*y
    print("{}分钟后，y的数量为{}。".format(n,y))
shiyi(60)