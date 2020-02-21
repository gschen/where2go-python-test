# coding=utf-8

'''
第八题：耐摔指数
题目描述
 
x星球的居民脾气不太好，但好在他们生气的时候唯一的异常举动是：摔手机。
各大厂商也就纷纷推出各种耐摔型手机。x星球的质监局规定了手机必须经过耐摔测试，并且评定出一个耐摔指数来，之后才允许上市流通。

x星球有很多高耸入云的高塔，刚好可以用来做耐摔测试。塔的每一层高度都是一样的，与地球上稍有不同的是，他们的第一层不是地面，而是相当于我们的2楼。

如果手机从第7层扔下去没摔坏，但第8层摔坏了，则手机耐摔指数=7。
特别地，如果手机从第1层扔下去就坏了，则耐摔指数=0。
如果到了塔的最高层第n层扔没摔坏，则耐摔指数=n

为了减少测试次数，从每个厂家抽样3部手机参加测试。

如果已知了测试塔的高度，并且采用最佳策略，在最坏的运气下最多需要测试多少次才能确定手机的耐摔指数呢？

输入数据，一个整数n（3<n<10000）,表示测试塔的高度。
输出一个整数，表示最多测试多少次。

例如：
输入：
3

程序应该输出：
2

解释：
手机a从2楼扔下去，坏了，就把b手机从1楼扔；否则a手机继续3层扔下

再例如：
输入：
7

程序应该输出：
3

解释：
a手机从4层扔，坏了，则下面有3层，b,c 两部手机2次足可以测出指数；
若是没坏，手机充足，上面5,6,7 三层2次也容易测出。
'''