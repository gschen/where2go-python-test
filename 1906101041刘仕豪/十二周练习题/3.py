'''
切面条
-根高筋拉面，中间切-刀,可以得到2根面条。
如果先对折1次，中间切-刀,可以得到3根面条。
如果连续对折2次，中间切-刀，可以得到5根面条。
那么,连续对折10次，中间切-刀，会得到多少面条呢?
思路:
由于对折次数仅为10，数据规模并不大,可以通过手算简单的完成。
对折0次，得到2根;
对折1次，得到2*2- 1 = 3
对折2次，得到3 *2-1 = 5
对折3次，得到5 *2-1 = 9.
对折4次，得到9 * 2-1 = 17
对折5次，得到17 *2- 1 = 33
对折6次，得到33*2-1 = 65
对折7次，得到65*2-1=129
对折8次，得到129 * 2- 1 = 257
对折9次，得到257 * 2- 1 = 513
对折10次，得到513 *2- 1 = 1025 .
实，上面的思路就是一种递归，可以把这种思想通过代码实现。
递有基本递归与尾递归两种形式，本文分别进行了代码实现。
尾递在一定程度上可以提高程序效率,通常比基本递归多-个参数。
递归的本质就是栈，当然可以用栈实现,在数据规模特别大的时候要显式的使用栈，以防止栈溢出。
答案: 1025
'''
def qiemian(n):
    a,b = 2,3
    t = 0
    while t < n:
        a,b = b,2*b-1
        t += 1
    return a
